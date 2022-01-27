from command import *
from status import *
from recipe_module import *
# # todo = {}

# # for i in range(3):
# #     todo[i] = []

# # print(todo)
# # print(STATUS_POS_USABLE)

# # usable_place_num = [i for i in range(FRY_NUM) if STATUS_POS_USABLE['f{}'.format(i)]]

# # print(usable_place_num)

# # print(STATUS_POS)

# # print(ORDER_LIST)
# # for i in usable_place_num:
# #     f_pos = 'f{}'.format(i)
# #     status_f_pos = STATUS_POS[f_pos]
# recipe_array = [0] * 22

# # cmd = cmd_creation.init_cmds()
# # print(cmd.get_cooking_pos())
# # print(cmd)
# #cmd = cmd.cmd_creation.create_cmds(cmd,'w1','f1','shake1','ad')
# # for i in cmd.cmds:
# #     print(i)
def tmp(w_pos):
    STATUS_POS[w_pos] = '09'
    ORDER_LIST.append(w_pos)

STATUS_FRIED_TIME_UI['f1'] = 100
EARLY_FIN['f1'] = True
#STATUS_POS['f1'] = '09'
i = 7
#tmp('w{}'.format(i))
PREV_POS_DATA['f1'] = 0
STATUS_POS['f1'] = 'fried_09'
WAITING_POINT['w{}'.format(i)] = 'nothing'
RECIPE_DATA_APP[8] = [1]*22
recipe_array = RECIPE_DATA_APP[7] 
for i in range(10):
    print(RECIPE_DATA_APP[i])


print("Waiting point:", WAITING_POINT)

print("Order list : ",ORDER_LIST)
print("Status pos: ",STATUS_POS)
print("usable status pos: ",STATUS_POS_USABLE)
work = next_work("test work")

cmd = work.GetWork()
print(cmd.cmds)

# cmds = CommandJob()
# cmds.clear_commands()
# cmds.add_cmd(CMD_FRY_PICKUP('w0',10))

# cmd = cmds.get_next_job()
# cmd.start()
# print(cmds.current_job.__repr__())