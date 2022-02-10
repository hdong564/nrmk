from time import time
from time import sleep
from unittest import case
from indy.logic.commands import *
from status import *

class next_work():
    def __init__(self):
        self.usable_place_num = [i for i in range(FRY_NUM) if STATUS_POS_USABLE['f{}'.format(i)]]
        self.todo = {}
        for i in range(3):
            self.todo[i] = []

    def GetWork(self):
        self.MainLogic()
        print(f"\n**** TODO list ****\n{self.todo}")

        for i in range(3):
            for work in self.todo[i]:
                return work
        
        if (self.todo[0] == []) and (self.todo[1] == []) and (self.todo[2] == []):
            work = CommandJob()
            work.clear_commands()
            work.add_cmd(CMD_WAIT_CMD())
            return work
        return None

    def MainLogic(self):
        for i in self.usable_place_num:
            f_pos = 'f{}'.format(i)
            status_f_pos = STATUS_POS[f_pos]
            if status_f_pos != 'nothing':
                recipe_structure = self.GetRecipe(status_f_pos)
                self.FposLogic(recipe_structure,f_pos)    
            else:
                continue

        if len(ORDER_LIST) and (self.todo[0] == []):
            w_pos = ORDER_LIST[0]
            status_w_pos = STATUS_POS[w_pos]
            if status_w_pos != 'nothing':
                print(status_w_pos)
                recipe_structure = self.GetRecipe(status_w_pos)
                self.WposLogic(recipe_structure,w_pos)

    def GetRecipe(self,status_pos):
        '''return type: len 22 array and int -- tuple'''
        recipe_num = int(status_pos[-2:]) 
        recipe = Recipe(RECIPE_DATA_APP[recipe_num-1])
        return (recipe,recipe_num)

    def FposLogic(self,recipe_structure,f_pos):
        '''Logic for fry pos'''
        print("*************************fpos logic start!")
        recipe = recipe_structure[0]
        recipe_num = recipe_structure[1]
        status_f_pos = STATUS_POS[f_pos]
        status = ""
        if 'fried' in status_f_pos:
            c_pos = FRY_POS +"_"+ "fried"
            if (STATUS_FRIED_TIME_UI[f_pos] > recipe.total_time) or EARLY_FIN[f_pos] == True:
                cmd = CmdCreation(recipe,status,None,f_pos,c_pos)
                self.todo[0].append(cmd)
        c_pos = FRY_POS +"_" +"wait_shaking"
        
        if ('waitshaking1' in status_f_pos):
            shake_n = recipe.get_shakeNum() 
            if shake_n == 1:
                status = "shaked3_" + status_f_pos.replace("waitshaking1_","")
            if shake_n == 2:
                status = "shaked2_" + status_f_pos.replace("waitshaking1_","")
            if shake_n == 3:
                status = "shaked1_" + status_f_pos.replace("waitshaking1_","")
            cmd = CmdCreation(recipe,status,None,f_pos,c_pos)
            self.todo[2].append(cmd)

        elif "waitshaking2" in status_f_pos:
            status = "shaked2_"+ status_f_pos.replace("waitshaking2_","")
            cmd = CmdCreation(recipe,status,None,f_pos,c_pos)
            self.todo[2].append(cmd)

        elif "waitshaking3" in status_f_pos:
            status = "shaked3_"+ status_f_pos.replace("waitshaking3_","")
            cmd = CmdCreation(recipe,status,None,f_pos,c_pos)
            self.todo[2].append(cmd)

    def WposLogic(self,recipe_structure,w_pos):
        '''Logic for basket pos'''
        recipe = recipe_structure[0]
        recipe_num = recipe_structure[1]
        menu = recipe.get_menu()
        c_pos = BASKSET_POS
        check_count = 0
        status = ""
        for i in range(6):
            if (2<= i <= 3):
                continue
            if w_pos == 'w{}'.format(i) or w_pos == 'w{}'.format(i+2):
                f_pos = 'f{}'.format(check_count)
            check_count +=1
        #print("W_pos, f_pos checking.. done!", w_pos,"->",f_pos)
    
        # error handling #
        #print("###########",WAITING_POINT[w_pos])
        if STATUS_POS[f_pos] != 'nothing' or WAITING_POINT[w_pos] != 'nothing':
            if STATUS_POS[f_pos] != 'nothing':
                print("ERROR! - please remove f_pos basket")
            else: # waiting point empty
                print("ERROR! - please place w_pos bakset")

            del ORDER_LIST[0]
            ORDER_LIST.append(w_pos)
        # status selection #
        else:
            #status = self.get_status(recipe,status,w_pos)
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
            else: 
                status = None
            cmd = CmdCreation(recipe,status,w_pos,f_pos,c_pos)
            del ORDER_LIST[0]
            self.todo[1].append(cmd)


    def __del__(self):
        #print("next_work processing done!")
        pass