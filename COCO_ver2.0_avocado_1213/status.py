from time import time, sleep
import copy

CB_IP = "192.168.0.46"

GLOBAL_FLAG = {'run': False, 'test_mode': False, 'isChanged': False, 'menu_end1':False, 'menu_end2':False, 'menu_end3':False, 'menu_end4':False, 'menu_end5':False, 'menu_end6':False, 'menu_end7':False, 'menu_end8':False }

CHECK_FLAG = {'menu_check1':False, 'menu_check2':False, 'menu_check3':False, 'menu_check4':False, 'menu_check5':False, 'menu_check6':False, 'menu_check7':False, 'menu_check8':False }

FRY_NUM = 4 #fryer구 개수
# FRY_WAIT_NUM = 2 #대기공간 개수

WAIT_NUM = 8 #waintpoint 개수
BASKET_NUM = 8

ORDER_LIST = []

RECIPE_DATA_APP= [[0]*22 for i in range(10)]

END_COUNT = {'num' : 0}

WAITING_POINT = {'w0' : 'empty', 'w1' : 'empty', 'w2' : 'empty', 'w3' : 'empty',
                'w4' : 'empty' , 'w5' : 'empty' , 'w6' : 'empty' , 'w7' : 'empty'}

FIN_EMPTY = {'w0' : False, 'w1' : False, 'w2' : False, 'w3' : False,
                'w4' : False , 'w5' : False , 'w6' : False , 'w7' : False}

POS_DATA = [
    # # code, name, pickup_time, place_time, shake_time, air_shake
    (0,   'w0',   10,  10,  0,  0),
    (1,   'w1',   10,  10,  0,  0),
    (2,   'w2',   10,  10,  0,  0), 
    (3,   'w3',   10,  10,  0,  0),
    (4,   'w4',   10,  10,  0,  0), 
    (5,   'w5',   10,  10,  0,  0),
    (6,   'w6',   10,  10,  0,  0), 
    (7,   'w7',   10,  10,  0,  0), 
    (8,   'f0',   10,  10, 30, 20),
    (9,   'f1',   10,  10, 30, 20),
    (10,  'f2',   10,  10, 30, 20),
    (11,  'f3',   10,  10, 30, 20),
]

EARLY_FIN= {'f0' : False, 'f1' : False, 'f2' : False, 'f3' : False}

'''handling already cooking basket'''
COOKING_FLAG = dict([('w{}'.format(i), ['waiting recipe',0]) for i in range(BASKET_NUM)])

# 메뉴 : 치킨, 감자, 순살

# POS_STATE_DATA = [
#     #new
#     (0,  'nothing'                 ),
#     (1,  'empty'                   ), 
#     (11, 'bone'                    ),
#     (12, 'barebone'                ), 
#     (13, 'potato'                  ),
#     (14, 'cheeseball'              ),
#     (21, 'shaked1_bone'            ),
#     (22, 'shaked1_barebone'        ), 
#     (23, 'shaked1_potato'          ),
#     (24, 'shaked1_cheeseball'      ),
#     (31, 'waitshaking2_bone'       ),
#     (32, 'waitshaking2_barebone'   ),
#     (33, 'waitshaking2_potato'     ),
#     (34, 'waitshaking2_cheeseball' ),
#     (41, 'shaked2_bone'            ),
#     (42, 'shaked2_barebone'        ), 
#     (43, 'shaked2_potato'          ),
#     (44, 'shaked2_cheeseball'      ),
#     (51, 'waitshaking3_bone'       ),
#     (52, 'waitshaking3_barebone'   ),
#     (53, 'waitshaking3_potato'     ),
#     (54, 'waitshaking3_cheeseball' ),
#     (61, 'shaked3_bone'            ),
#     (62, 'shaked3_barebone'        ), 
#     (63, 'shaked3_potato'          ),
#     (64, 'shaked3_cheeseball'      ),
#     (71, 'fried_bone'              ),
#     (72, 'fried_barebone'          ),
#     (73, 'fried_potato'            ),
#     (74, 'fried_cheeseball'        ),
# ]

# RECIPE_DATA = [
#     #total time : bone 10, barebone 6, potato 3.5, cheeseball 2
#     ('bone',                   0.0*60), 
#     ('barebone',               0.0*60), 
#     ('potato',                 0.0*60), 
#     ('cheeseball',             0.0*60),#넣고 흔드는 작업시간 생각 30s
#     ('notshaked1_bone',        1.8*60),
#     ('waitshaking1_bone',      0.0*60),


#     ('shaked1_bone',           1.5*60),
#     ('shaked1_barebone',       1.5*60),
#     ('shaked1_potato',         1.1*60),
#     ('shaked1_cheeseball',     0.0*60),
#     ('waitshaking2_bone',      0.0*60),
#     ('waitshaking2_barebone',  0.0*60),
#     ('waitshaking2_potato',    0.0*60),
#     ('waitshaking2_cheeseball',0.0*60),
#     ('shaked2_bone',           1.5*60), #작업대강 30초 고려 합산 1분으로... 
#     ('shaked2_barebone',       1.5*60),
#     ('shaked2_potato',         1.1*60),
#     ('shaked2_cheeseball',     0.0*60),
#     ('waitshaking3_bone',      0.0*60),
#     ('waitshaking3_barebone',  0.0*60),
#     ('waitshaking3_potato',    0.0*60),
#     ('waitshaking3_cheeseball',0.0*60),
#     ('shaked3_bone',           6.5*60), 
#     ('shaked3_barebone',       3.0*60),
#     ('shaked3_potato',         1.0*60),
#     ('shaked3_cheeseball',     1.8*60),
# ]

ROBOT_SYSTEM_DATA = [
    ('not_ready'       ), 
    ('ready'           ), 
    ('program_running' ),
    ('collision'       ),
    ('error'           ),
    ('paused'          ),
]

BASE_SYSTEM_DATA = [
    'not_ready',
    'ready',
    'emergency',
    'moving',
    'alarm',
    'freerun'
]

# dict으로 이전 위치 저장
PREV_POS_DATA = {}

CONTY_PROGRAM_IS_RUNNING = False
CONTY_DIRECT_TEACHING_IS_RUNNING = False

UI_REQUEST_PAUSE            = 0b0000000000000001
UI_REQUEST_RESUME           = 0b0000000000000010
UI_REQUEST_STOP             = 0b0000000000000100
UI_REQUEST_DT               = 0b0000000000001000 #direct teaching
UI_REQUEST_CMD              = 0b0000000000010000
UI_REQUEST_ENDT_ON          = 0b0000000000100000
UI_REQUEST_ENDT_OFF         = 0b0000000001000000
UI_REQUEST_GOHOME           = 0b0000000010000000
UI_REQUEST_INIT_PROGRAM     = 0b0010000000000000
UI_REQUEST_TEST             = 0b1000000000000000

STATUS_ROBOT = {"system" : "not_ready", "direct_teaching": False, "holding" : "nothing", "ui_request": 0, "ui_cmd": -1, "working":0}
STATUS_POS = dict([(n, 'nothing') for _, n, *_ in POS_DATA])  #name 'nothing'

STATUS_POS_USABLE = dict([('f{}'.format(i), True) for i in range(FRY_NUM)])
STATUS_FRIED_TIME = dict([('f{}'.format(i), 99999) for i in range(FRY_NUM)])
STATUS_NEXT_WORK = ['nothing']

STATUS_FRIED_TIME_UI = dict([('f{}'.format(i), 0) for i in range(FRY_NUM)])


'''for selecting menu'''
MAIN_MENU  = 1
SIDE_MENU  = 2
DRINK_MENU = 3

pos_nc = dict([(n, c) for c, n, *_ in POS_DATA]) #nametocode
# pos_map = dict([[n, (c, n, t_pck, t_plc, t_s, t_as)] for c, n, t_pck, t_plc, t_s, t_as in POS_DATA])

# pos_state_nc = dict([(n, c) for c, n in POS_STATE_DATA]) #name code
# pos_state_cn = dict([(c, n) for c, n in POS_STATE_DATA]) #code name
# recipe_nt = dict([(n, t) for n, t in RECIPE_DATA]) #name, time

def get_frying_time(menu):
    if (menu != 'nothing'):
        recipe_num = int(menu[-2:])
        if recipe_num == 0:
            return 99999
        elif ('notshaked1' in menu):
            return RECIPE_DATA_APP[recipe_num-1][15]
        elif ('waitshaking1' in menu):
            return 0
        elif ('shaked1' in menu):
            return RECIPE_DATA_APP[recipe_num-1][16]
        elif ('waitshaking2' in menu):
            return 0
        elif ('shaked2' in menu):
            return RECIPE_DATA_APP[recipe_num-1][17]    
        elif ('waitshaking3' in menu):
            return 0
        elif ('shaked3' in menu):
            return RECIPE_DATA_APP[recipe_num-1][18]    
        else:
            return 0


# helper function
def TransToSec(min,sec):
    return 60*min + sec

# Recipe structure
class Recipe:
    def __init__(self,Recipe_Array):
        self.is_shake1 = Recipe_Array[2]
        self.is_shake2 = Recipe_Array[6]
        self.is_shake3 = Recipe_Array[10]
        self.array = Recipe_Array
        self.total_time   = TransToSec(Recipe_Array[0], Recipe_Array[1])
        self.until_shake1 = TransToSec(Recipe_Array[4],Recipe_Array[5])
        self.until_shake2 = TransToSec(Recipe_Array[8],Recipe_Array[9]) 
        self.until_shake3 = TransToSec(Recipe_Array[12], Recipe_Array[13])
        self.is_main  = Recipe_Array[19] # Chicken or something
        self.is_side  = Recipe_Array[20] # Fried potato or something
        self.is_drink = Recipe_Array[21] # Beer!
    # def TransToSec(min,sec):
    #     return 60*min + sec
    def no_shaking(self):
        if not self.is_shake1 and not self.is_shake2 and not self.is_shake3:
            return 1
        else: 
            return 0
    def get_menu(self):
        if self.is_main:
            return 1
        elif self.is_side:
            return 2
        elif self.is_drink:
            return 3


    def intervals_shake1(self):
        result = []
        result.append(self.until_shake1)
        result.append(self.total_time - self.until_shake1)
        return result
        # result = [intv1 < intv2]
    def intervals_shake2(self):
        result = []
        result.append(self.until_shake1)
        result.append(self.until_shake2 - self.until_shake1)
        result.append(self.total_time - self.until_shake2)
        return result
        # result = [intv1 < intv2 < intv3]
    def intervals_shake3(self):
        result = []
        result.append(self.until_shake1)
        result.append(self.until_shake2 - self.until_shake1)
        result.append(self.until_shake3 - self.until_shake2)
        result.append(self.total_time - self.until_shake3)
        return result
        # result = [intv1 < intv2 < intv3 < intv4]
    def total_time(self):
        result = []
        result.append(self.until_shake2 - self.until_shake1)
        result.append(self.total_time - self.until_shake2 - self.until_shake1)
        val = TransToSec(self.array[0], self.array[1])


# def get_status_code(pos):
#     return pos_state_nc[STATUS_POS[pos]]