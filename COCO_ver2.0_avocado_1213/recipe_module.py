

from telnetlib import STATUS
from time import time
from time import sleep
from unittest import case
from indy.logic.commands import *
from status import *

class next_work():
    def __init__(self,name):
        self.name = name
        self.usable_place_num = [i for i in range(FRY_NUM) if STATUS_POS_USABLE['f{}'.format(i)]]
        self.todo = {}
        for i in range(3):
            self.todo[i] = []

    def GetWork(self):
        print("Main logic start ...")
        self.MainLogic()
        for i in range(3):
            for work in self.todo[i]:
                return work
        for cmds in self.todo:
            if cmds:
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

    def FposLogic(self,recipe,f_pos):
        print("Fpos logic processing...")
        recipeArray = recipe[0]
        recipeNum = recipe[1]
        #print(recipeArray.array, recipeNum)


    def WposLogic(self,recipe,w_pos):
        print("Wpos logic processing...")
        print("Wpos logic Done!")
        check_count = 0
        for i in range(6):
            if (2<= i <= 3):
                continue
            if w_pos == 'w{}'.format(i) or w_pos == 'w{}'.format(i+2):
                print("checking: ",'w{}'.format(i),'w{}'.format(i+2))
                f_pos = 'f{}'.format(check_count)
                print(f_pos)
            check_count +=1
        print("W_pos, f_pos chekcking.. done!", w_pos,f_pos)


    def MainLogic(self):
        for i in self.usable_place_num:
            f_pos = 'f{}'.format(i)
            status_f_pos = STATUS_POS[f_pos]
            print("checking f_pos ... ",f_pos)
            if status_f_pos != 'nothing':
                print("Fpos logic Start!")
                recipe = self.GetRecipe(status_f_pos)
                self.FposLogic(recipe,f_pos)    
            else:
                continue

        if len(ORDER_LIST) and (self.todo[0] == []):
            w_pos = ORDER_LIST[0]
            status_w_pos = STATUS_POS[w_pos]
            print("checking w_pos...")
            if status_w_pos != 'nothing':
                print("Wpos logic Start!")
                recipe = self.GetRecipe(status_w_pos)[0]
                self.WposLogic(recipe,w_pos)

    def __del__(self):
        print(f"delete {self.name}")