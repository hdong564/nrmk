

from calendar import SATURDAY
from telnetlib import STATUS
from time import time
from time import sleep
from unittest import case
from command import *
from status import *

class next_work():
    def __init__(self,name):
        self.name = name
        self.usable_place_num = [i for i in range(FRY_NUM) if STATUS_POS_USABLE['f{}'.format(i)]]
        self.todo = {}
        for i in range(3):
            self.todo[i] = []

    def GetWork(self):
        print("# Main logic start ...")
        self.MainLogic()
        print(self.todo)
        for i in range(3):
            for work in self.todo[i]:
                return work
        
        if (self.todo[0] == []) and (self.todo[1] == []) and (self.todo[2] == []):
            work = CommandJob()
            work.clear_commands()
            work.add_cmd(CMD_WAIT_CMD())
            return work
        return None


    def GetRecipe(self,status_pos):
        '''return type: len 22 array and int -- tuple'''
        recipe_num = int(status_pos[-2:]) 
        recipe = Recipe(RECIPE_DATA_APP[recipe_num-1])
        return (recipe,recipe_num)

    def FposLogic(self,recipe_structure,f_pos):
        '''Logic for fry pos'''
        print("Fpos logic processing...", f_pos)
        recipe = recipe_structure[0]
        recipe_num = recipe_structure[1]
        status_f_pos = STATUS_POS[f_pos]
        status = ""
        if 'fried' in status_f_pos:
            c_pos = FRY_POS + "fried"
            if (STATUS_FRIED_TIME_UI[f_pos] > recipe.total_time) or EARLY_FIN[f_pos] == True:
                ''' gotta update'''
                cmd = CmdCreation(recipe,status,None,f_pos,c_pos)
                self.todo[0].append(cmd)
        c_pos = FRY_POS + "wait_shaking"
        for i in range(1,SHAKING_NUM+1):
            if "waitshaking{}".format(i) in status_f_pos:
                for j in range(1,SHAKING_NUM):
                    if recipe.get_shakeNum() == j:
                        status = "shaked{}".format(SHAKING_NUM-j+1) + status_f_pos.replace("waitshaking{}_".format(i),"")
                        break
        print(status)
        cmd = CmdCreation(recipe,status,None,f_pos,c_pos)
        self.todo[2].append(cmd)
        # cmd = cmd_creation.init_cmds()
        # cmd = cmd_creation.create_cmds(cmd,None,f_pos,status)
        # self.todo[2].append(cmd)

        print("********* Fpos logic Done! **********")

    def WposLogic(self,recipe_structure,w_pos):
        '''Logic for basket pos'''
        print("Wpos logic processing...")
        recipe = recipe_structure[0]
        recipe_num = recipe_structure[1]
        #print(recipe.array)
        menu = recipe.get_menu()
        print("menu: ",menu)
        c_pos = BASKSET_POS
        check_count = 0
        status = ""

        for i in range(6):
            if (2<= i <= 3):
                continue
            if w_pos == 'w{}'.format(i) or w_pos == 'w{}'.format(i+2):
                f_pos = 'f{}'.format(check_count)
            check_count +=1

        print("W_pos, f_pos checking.. done!", w_pos,"->",f_pos)
    
        # error handling #
        if STATUS_POS[f_pos] != 'nothing' or WAITING_POINT[w_pos] != 'nothing':
            print("ERROR! - please remove fry basket")
            del ORDER_LIST[0]
            ORDER_LIST.append(w_pos)
        # status selection #
        else:
            if recipe.no_shake:
                    status = "shaked3_" + STATUS_POS[w_pos]
            elif recipe.is_shake1:#
                if recipe.immediate_shake:
                    status = "shaked3_" + STATUS_POS[w_pos]
                else:
                    status = "notshaked1_" + STATUS_POS[w_pos]
            elif recipe.is_shake2:
                if recipe.immediate_shake:
                    status = "shaked2_" + STATUS_POS[w_pos]
                else: 
                    status = "notshaked1_" + STATUS_POS[w_pos] 
            elif recipe.is_shake3:
                if recipe.immediate_shake:
                    status = "shaked1_" + STATUS_POS[w_pos]
                else: 
                    status = "notshaked1_" + STATUS_POS[w_pos]
            
            print(status, w_pos, f_pos,c_pos)
            cmd = CmdCreation(recipe,status,w_pos,f_pos,c_pos)
            print(cmd.cmds)
            del ORDER_LIST[0]
            self.todo[1].append(cmd)
        print("######## Wpos logic Done! #########")

    def MainLogic(self):
        for i in self.usable_place_num:
            f_pos = 'f{}'.format(i)
            status_f_pos = STATUS_POS[f_pos]
            #print("checking f_pos ... ",f_pos)
            if status_f_pos != 'nothing':
                print("******** Fpos logic Start! *********")
                recipe_structure = self.GetRecipe(status_f_pos)
                self.FposLogic(recipe_structure,f_pos)    
            else:
                continue

        if len(ORDER_LIST) and (self.todo[0] == []):
            w_pos = ORDER_LIST[0]
            status_w_pos = STATUS_POS[w_pos]
            print("checking w_pos...")
            if status_w_pos != 'nothing':
                print(status_w_pos)
                print("######### Wpos logic Start! #########")
                recipe_structure = self.GetRecipe(status_w_pos)
                self.WposLogic(recipe_structure,w_pos)

    def __del__(self):
        print(f"delete {self.name}")