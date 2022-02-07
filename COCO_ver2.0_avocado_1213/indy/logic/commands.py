from status import *

COMMAND_TYPE_LIMB = "limb" # robot hand
COMMAND_TYPE_STATUS = "status"
COMMAND_TYPE_COOKING_TIME = "cooking_time"

#명령값(직접변수값) B600
COMMAND_LIMB_HOME                   = 1
COMMAND_LIMB_HOME_POINT_2           = 2   #test2#
# COMMAND_LIMB_HOME_TO_READY          = 5
# COMMAND_LIMB_READY_TO_HOME          = 6
# COMMAND_LIMB_READY_PICKUP           = 10
# COMMAND_LIMB_READY_PLACE            = 11
# COMMAND_LIMB_READY_PICKUP_WO_SHAKE  = 12
COMMAND_LIMB_FRY_PICKUP             = 20
COMMAND_LIMB_FRY_PICK_MOVE          = 30

COMMAND_LIMB_FRY_PLACE              = 40
COMMAND_LIMB_FRY_PLACE_END          = 50

COMMAND_LIMB_WAIT_PICKUP            = 60
COMMAND_LIMB_WAIT_PLACE             = 80
# COMMAND_LIMB_FRY_SHAKE              = 100   #no use
# COMMAND_LIMB_WAITING_PICKUP         = 120
COMMAND_LIMB_AIR_WAIT              = 130
COMMAND_LIMB_AIR_SHAKE              = 140
COMMAND_LIMB_FRY_SHAKE              = 150
# COMMAND_LIMB_FRY_PICKUP_N_SHAKE     = 160
# COMMAND_LIMB_FRY_PLACE_N_SHAKE      = 180
# COMMAND_LIMB_CUSTOM_MOTION          = 200
# COMMAND_LIMB_FINISH                 = 255
COMMAND_LIMB_WAIT_CMD               = 3 

'''commands for Fried 'Potato' '''
#COMMAND_LIMB_POTATO_PICKUP = 200
COMMAND_LIMB_POTATO_PLACE_MACHINE = 200
COMMAND_LIMB_POTATO_GET_WAIT = 210
COMMAND_LIMB_POTATO_PICKUP = 220
'''All consts above are B variables'''  


class CommandParam():
    def __init__(self, cmd_type: str, params):
        self.type = cmd_type
        self.params = params

class CommandBase():
    def __init__(self, pos, motion_time=0, pos1=None):
        self.pos = pos
        self.pos_code = pos_nc[pos]
        self.motion_time = motion_time
        self.pos1 = pos1
# class CMD_WAIT_PLACE(CommandBase):
#     def obtain_commands(self):
#         return [
#             CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_WAIT_PLACE + int(self.pos[1:])),
#             # CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_HOME)
#         ]
    def __repr__(self):
        return f"< cmd: {type(self)}>"
#        return f"< cmd {self.pos} : {self.pos_code} : {type(self)}>"

    def obtain_commands(self):
        pass

    def get_motion_time(self):
        return self.motion_time
    
    def start(self):
        pass
    
    def done(self):
        pass

class CMD_CUSTOM(CommandBase):
    def __init__(self, target, cmd):
        self.pos = "custom"
        self.pos_code = 0
        self.motion_time = 0
        self.target = target
        self.cmd = cmd

    def obtain_commands(self):
        return [CommandParam(self.target, self.cmd)]

class CMD_CHANGE_STATUS(CommandBase):
    def __init__(self, pos, status):
        super().__init__(pos, 0)
        self.status = status

    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_STATUS, (
                self.pos,
                self.status
            ))
        ]

class CMD_SET_COOKING_TIME(CommandBase):
    def __init__(self, pos, time=None):
        super().__init__(pos, 0)
        self.cooking_time = time

    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_COOKING_TIME, self.cooking_time)
        ] if self.cooking_time is not None else [
            CommandParam(COMMAND_TYPE_COOKING_TIME, get_frying_time(STATUS_POS[self.pos]))
        ]

class CMD_AIR_SHAKE(CommandBase):
    def __init(self, pos):
        super().__init__(pos, 0)

    def start(self):
        STATUS_ROBOT["working"] = 2
        

    def obtain_commands(self):
        r_n = int(STATUS_POS[self.pos][-2:])
        s_h = RECIPE_DATA_APP[r_n-1][14]

        return ([CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_AIR_WAIT + int(self.pos[1:]))] +
            [CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_AIR_SHAKE + int(self.pos[1:]))]*s_h)

    def done(self):        
        STATUS_POS[self.pos] = "nothing"

class CMD_WAIT_PLACE(CommandBase):
    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_WAIT_PLACE + int(self.pos[1:])),
            # CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_HOME)
        ]
    
    def done(self):
        STATUS_POS[self.pos] = STATUS_ROBOT["holding"]
        STATUS_ROBOT["holding"] = "nothing"
        GLOBAL_FLAG['isChanged'] = True        
        STATUS_FRIED_TIME_UI[self.pos1] = 0
        STATUS_ROBOT["working"] = 0
        if self.pos == 'w0':
            GLOBAL_FLAG['menu_end1'] = True
        elif self.pos == 'w1':
            GLOBAL_FLAG['menu_end2'] = True
        elif self.pos == 'w2':
            GLOBAL_FLAG['menu_end3'] = True
        elif self.pos == 'w3':
            GLOBAL_FLAG['menu_end4'] = True
        elif self.pos == 'w4':
            GLOBAL_FLAG['menu_end5'] = True
        elif self.pos == 'w5':
            GLOBAL_FLAG['menu_end6'] = True
        elif self.pos == 'w6':
            GLOBAL_FLAG['menu_end7'] = True
        elif self.pos == 'w7':
            GLOBAL_FLAG['menu_end8'] = True

class CMD_WAIT_PICKUP(CommandBase):
    def start(self):
        STATUS_ROBOT["working"] = 3

    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_WAIT_PICKUP + int(self.pos[1:])),
            # CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_HOME)
        ]
    
    def done(self):
        STATUS_ROBOT["holding"] = STATUS_POS[self.pos]
        STATUS_POS[self.pos] = "nothing"
          
class CMD_FRY_PLACE(CommandBase):    
    def obtain_commands(self):
        r_n = int(STATUS_POS[self.pos][-2:])
        s_h = RECIPE_DATA_APP[r_n-1][3]

        return ([CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PLACE + int(self.pos[1:]))] + 
        [CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_SHAKE + int(self.pos[1:]))] * s_h + 
        [CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PLACE_END + int(self.pos[1:]))])
    
    def done(self):
        if STATUS_ROBOT["holding"] != "nothing":
            STATUS_POS[self.pos] = STATUS_ROBOT["holding"]
            STATUS_ROBOT["holding"] = "nothing"
            STATUS_FRIED_TIME[self.pos] = get_frying_time(STATUS_POS[self.pos])
            STATUS_ROBOT["working"] = 0

class CMD_FRY_PLACE_SHAKENONE(CommandBase):
    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PLACE + int(self.pos[1:])),
            # CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_SHAKE + int(self.pos[1:])),
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PLACE_END + int(self.pos[1:])),
        ]
    
    def done(self):
        if STATUS_ROBOT["holding"] != "nothing":
            STATUS_POS[self.pos] = STATUS_ROBOT["holding"]
            STATUS_ROBOT["holding"] = "nothing"
            STATUS_FRIED_TIME[self.pos] = get_frying_time(STATUS_POS[self.pos])
            STATUS_ROBOT["working"] = 0       

class CMD_FRY_PICKUP(CommandBase):
    def start(self):
        STATUS_ROBOT["working"] = 3
    
    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PICKUP + int(self.pos[1:])),
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PICK_MOVE + int(self.pos[1:])),
        ]
    
    def done(self):
        STATUS_ROBOT["holding"] = STATUS_POS[self.pos]
        # STATUS_POS[self.pos] = "nothing"

class CMD_FRY_PICKUP_N_SHAKE(CommandBase):
    def start(self):
        STATUS_ROBOT["working"] = 1

    def obtain_commands(self):
        r_n = int(STATUS_POS[self.pos][-2:])
        #흔들기 몇번쨰인지 찾기        
        if 'waitshaking1' in STATUS_POS[self.pos]:
            s_h = RECIPE_DATA_APP[r_n-1][3]
        elif 'waitshaking2' in STATUS_POS[self.pos]:
            s_h = RECIPE_DATA_APP[r_n-1][7]
        elif 'waitshaking3' in STATUS_POS[self.pos]:
            s_h = RECIPE_DATA_APP[r_n-1][11]
        else:
            s_h = 1

        # return [
        #     CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PICKUP + int(self.pos[1:])),
        #     CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_SHAKE + int(self.pos[1:])),
        #     CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PLACE_END + int(self.pos[1:])),
        # ]
        return ([CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PICKUP + int(self.pos[1:]))] + 
        [CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_SHAKE + int(self.pos[1:]))] * s_h + 
        [CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_FRY_PLACE_END + int(self.pos[1:]))])

    def done(self):
        prev_time = STATUS_FRIED_TIME[self.pos]
        time = get_frying_time(STATUS_POS[self.pos])
        if prev_time < 0:
            time += prev_time
            
        print("CMD_FRY_PICKUP_N_SHAKE COOKING_TIME CHANGED:", self.pos, prev_time, "->", f"{time} ({get_frying_time(STATUS_POS[self.pos])})")
        STATUS_FRIED_TIME[self.pos] = time

'''
(next three cmds): for potato machine
CMD_POTATO_PLACE_MACHINE: param 200 
CMD_POTATO_GET_WAIT: param 210
CMD_POTATO_PLACE_FRY_SHAKE: param 220
'''
class CMD_POTATO_PLACE_MACHINE(CommandBase):
    # __init__ -> w_pos only
    def start(self):
        if STATUS_POS[self.pos] == "nothing":
            STATUS_POS[self.pos] = "potato_holding"
        
    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_POTATO_PLACE_MACHINE + int(self.pos[1:]))
        ]
    def done(self):
        STATUS_POS[self.pos] = "potato_get"
        
# test commit
class CMD_POTATO_GET_WAIT(CommandBase):
    def __init__(self,w_pos,size):
        self.w_pos = w_pos
        self.size = size
    def start(self):
        if STATUS_POS[self.pos] == "potato_get":
            def cal_extraction_time(size):
                return (3*size -1)
            POTATO_SIZE.append(self.size)
            POTATO_EXTRACTION_TIMES.append(cal_extraction_time(self.size))
        else: 
            print("ERROR!! - wrong direction of flow(Cmd-potato-get-wait")

    def obtain_commands(self):
        for i in range(2,5):
            if POTATO_SIZE[0] == i:
                return [CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_POTATO_GET_WAIT+i-2)]
        
        print("ERROR!! - no potato size..")
        return None
        # 210 -> S size
        # 211 -> M size
        # 212 -> L size
    def done(self):
        STATUS_POS[self.pos] = "potato_pickup"
        del POTATO_SIZE[0]
        del POTATO_EXTRACTION_TIMES[0]
        
class CMD_POTATO_PICKUP(CommandBase):
    
    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_POTATO_PICKUP + int(self.pos))
        ]
    def done(self):
        STATUS_POS[self.pos] = "nothing"

class CMD_WAIT_CMD(CommandBase):
    def start(self):
        STATUS_ROBOT["working"] = 0

    def __init__(self):
        self.pos = "readymotion"
        self.pos_code = 0
        self.motion_time = 0

    def obtain_commands(self):
        return [
            CommandParam(COMMAND_TYPE_LIMB, COMMAND_LIMB_WAIT_CMD)
        ]

class CommandJob():
    def __init__(self):
        self.current_job = None
        self.current_job_idx = -1
        self.cmds = []
        self.cooking_pos = None
        self.recipe_time = None
        self.prev_waiting_point = None
    def add_cmd(self, cmd: CommandBase):
        self.cmds.append(cmd)
        return self

    def clear_commands(self):
        self.cmds.clear()
        return self
    
    def set_cooking_pos(self, pos):
        self.cooking_pos = pos
        return self
    
    def get_cooking_pos(self):
        return self.cooking_pos
    
    def set_recipe_time(self, time):
        self.recipe_time = time
        return self
    
    def get_recipe_time(self):
        return self.recipe_time

    def get_motion_time(self):
        return sum([cmd.get_motion_time() for cmd in self.cmds])
    
    def get_next_job(self):
        if self.current_job_idx + 1 == len(self.cmds):
            return None
        self.current_job_idx += 1
        self.current_job = self.cmds[self.current_job_idx]
        return self.current_job
    
    def get_current_job(self):
        return self.current_job
def CmdCreation(recipe,status,w_pos,f_pos,c_pos):
    print("cooking_pos: ", c_pos)
    cmd = CommandJob()
    cmd.clear_commands()
    menu = recipe.get_menu()
    if c_pos == FRY_POS +"_"+ "fried":
        print("cmd fry pickup, cmd air shake, cmd wait place")
        cmd.add_cmd(CMD_FRY_PICKUP(f_pos,10))
        cmd.add_cmd(CMD_AIR_SHAKE(f_pos))
        #print("here")
        cmd.add_cmd(CMD_WAIT_PLACE(PREV_POS_DATA[f_pos], 10, pos1 = f_pos))
        cmd.set_cooking_pos(f_pos)
        print("Fry fin pos->", PREV_POS_DATA[f_pos]) #test
        EARLY_FIN[f_pos] = False
        return cmd
    elif c_pos == FRY_POS +"_"+ "wait_shaking":
        print(f"(menu: {menu}) frying basket processing ...")
        cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
        cmd.set_cooking_pos(f_pos)
        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
        return cmd
    elif c_pos == BASKSET_POS:
        '''menu num should be read from UI'''
        if menu == 0: # chicken
            print(f"(menu: {menu}) basket processing ...")
            cmd.add_cmd(CMD_WAIT_PICKUP(w_pos,10))
            if not recipe.immediate_shake or recipe.no_shake:
                cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos,10)) 
            else:
                cmd.add_cmd(CMD_FRY_PLACE(f_pos,10))
            cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos,time = get_frying_time(status)))
            cmd.add_cmd(CMD_CHANGE_STATUS(f_pos,status))
            cmd.set_cooking_pos(f_pos)
            PREV_POS_DATA[f_pos] = w_pos
            return cmd

        elif 2 <= menu <= 4:
            print("menu: Fried Potato")
            cmd.add_cmd(CMD_WAIT_PICKUP(w_pos,10))
            cmd.add_cmd(CMD_POTATO_PLACE_MACHINE(w_pos,10))
            cmd.add_cmd(CMD_POTATO_GET_WAIT(w_pos,menu)) # 
            cmd.add_cmd(CMD_POTATO_PICKUP(w_pos,10)) # comeback to wait pickup place
            if not recipe.immediate_shake or recipe.no_shake:
                cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos,10))
            else:
                cmd.add_cmd(CMD_FRY_PLACE(f_pos,10))
            cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos,time = get_frying_time(status)))
            cmd.add_cmd(CMD_CHANGE_STATUS(f_pos,status))
            cmd.set_cooking_pos(f_pos)
        elif menu == 5:
            print("menu: Beer!")
        else:
            print("ERROR!! - no menu" )

