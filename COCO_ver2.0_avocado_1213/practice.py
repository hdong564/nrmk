from indy.logic.commands import *
from indy.logic.recipe_logic import *
from status import *

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