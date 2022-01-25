

from indy.logic.commands import *
from status import *
from recipe_module import *
# todo = {}

# for i in range(3):
#     todo[i] = []

# print(todo)
# print(STATUS_POS_USABLE)

# usable_place_num = [i for i in range(FRY_NUM) if STATUS_POS_USABLE['f{}'.format(i)]]

# print(usable_place_num)

# print(STATUS_POS)

# print(ORDER_LIST)
# for i in usable_place_num:
#     f_pos = 'f{}'.format(i)
#     status_f_pos = STATUS_POS[f_pos]
recipe_array = [0] * 22

# cmd = cmd_creation.init_cmds()
# print(cmd.get_cooking_pos())
# print(cmd)
#cmd = cmd.cmd_creation.create_cmds(cmd,'w1','f1','shake1','ad')
# for i in cmd.cmds:
#     print(i)
def tmp(w_pos):
    STATUS_POS[w_pos] = '09'
    ORDER_LIST.append(w_pos)

STATUS_POS['f1'] = '09'
i = 7
tmp('w{}'.format(i))
print("Order list : ",ORDER_LIST)
print("Status pos: ",STATUS_POS)
print("usable status pos: ",STATUS_POS_USABLE)
work = next_work("test work")

print(work.GetWork())