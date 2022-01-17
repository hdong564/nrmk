from os import path as op
import yaml, os

CONFIG_FILEPATH = op.join(op.abspath(op.dirname(__file__)), "config.yml")

CONFIG_KEY_ROBOT_DOF            = "robot_dof"
CONFIG_KEY_DB_HOST              = "db_host"
CONFIG_KEY_DB_NAME              = "db_name"
CONFIG_KEY_DB_USER              = "db_user"
CONFIG_KEY_DB_PWD               = "db_pwd"
CONFIG_KEY_DB_TIMEOUT           = "db_timeout"
CONFIG_KEY_DB_LOGIN_TIMEOUT     = "db_login_timeout"
CONFIG_KEY_DB_CHARSET           = "db_charset"
CONFIG_KEY_ICE_ONLY             = "ice_only"
CONFIG_KEY_WATER_ONLY           = "water_only"
CONFIG_KEY_ICE_AND_WATER        = "ice_and_water"
CONFIG_KEY_COFFEE_MAP           = "coffee_map"
CONFIG_KEY_COFFEE_EXPIRY_TIME   = "coffee_expiry_time"
CONFIG_KEY_CUP_DISP_PACKET_LEN  = "cup_disp_packet_len"
CONFIG_KEY_ICE_DISP_PACKET_LEN  = "ice_disp_packet_len"
CONFIG_KEY_MILK_REFRESH_DURATION= "milk_refresh_duration"
CONFIG_KEY_LIFT_DELAY           = "lift_delay"
CONFIG_KEY_LIFT_CUP_DELAY       = "lift_cup_delay"
CONFIG_KEY_ESPRESSO_MACHINE_SHOT_DELAY_1 = "espresso_machine_shot_delay_1"
CONFIG_KEY_ESPRESSO_MACHINE_SHOT_DELAY_2 = "espresso_machine_shot_delay_2"
CONFIG_KEY_ESPRESSO_MACHINE_LONG_DELAY_1 = "espresso_machine_long_delay_1"
CONFIG_KEY_ESPRESSO_MACHINE_LONG_DELAY_2 = "espresso_machine_long_delay_2"

ESPRESSO_SHOT_DELAY_KEY_LIST = [
    CONFIG_KEY_ESPRESSO_MACHINE_SHOT_DELAY_1,
    CONFIG_KEY_ESPRESSO_MACHINE_SHOT_DELAY_2
]

ESPRESSO_LONG_DELAY_KEY_LIST = [
    CONFIG_KEY_ESPRESSO_MACHINE_LONG_DELAY_1,
    CONFIG_KEY_ESPRESSO_MACHINE_LONG_DELAY_2
]

BUNDLE_KEY_COFFEE_DATA = "coffee_data"

INDY_ADDR_COMMAND = 0
INDY_ADDR_HOT_ICE = 10
INDY_ADDR_MENU = 11
INDY_ADDR_CM_SLOT = 20
INDY_ADDR_LIFT_SLOT = 50

INDY_CMD_IDLE               = 0
INDY_CMD_MOUNT_FILTER       = 1
INDY_CMD_MOVE_CUP           = 10
INDY_CMD_MOVE_ICE           = 11
INDY_CMD_MOVE_MILK          = 12
INDY_CMD_MOVE_HOT_WATER     = 13
INDY_CMD_MOVE_CM_SLOT       = 14
INDY_CMD_MOVE_LIFT_SLOT     = 15
INDY_CMD_MOVE_TRASH         = 16
INDY_CMD_CLEAN              = 100
# INDY_CMD_REFRESH_MILK       = 101
INDY_CMD_WAIT_POS           = 101

INDY_DI_ADDR_BTN_RUN_STATE      = 0
INDY_DI_ADDR_BTN_RESET          = 1
INDY_DI_ADDR_CUP_DETECT         = 2 # Not used
INDY_DI_ADDR_LIFT1_STATE_UP     = 3
INDY_DI_ADDR_LIFT1_STATE_DOWN   = 4
INDY_DI_ADDR_LIFT2_STATE_UP     = 5
INDY_DI_ADDR_LIFT2_STATE_DOWN   = 6
INDY_DI_ADDR_LIFT3_STATE_UP     = 7
INDY_DI_ADDR_LIFT3_STATE_DOWN   = 8
INDY_DI_ADDR_HAND_PROTECTION    = 9
INDY_DI_ADDR_LIFT1_CUP_EXISTS   = 10
INDY_DI_ADDR_LIFT2_CUP_EXISTS   = 11
INDY_DI_ADDR_LIFT3_CUP_EXISTS   = 12
INDY_DI_ADDR_AIR_PRESS_DETECT   = 13 # Not used

INDY_DO_ADDR_ONE_SHOT_LEFT      = 0
INDY_DO_ADDR_TWO_SHOT_LEFT      = 1
INDY_DO_ADDR_ONE_SHOT_RIGHT     = 2
INDY_DO_ADDR_TWO_SHOT_RIGHT     = 3
INDY_DO_ADDR_HOT_WATER_FULL     = 4
INDY_DO_ADDR_HOT_WATER_MEDIUM   = 5
INDY_DO_ADDR_COLD_WATER_FULL    = 6
INDY_DO_ADDR_COLD_WATER_MEDIUM  = 7
INDY_DO_ADDR_LIFT1_UP           = 8
INDY_DO_ADDR_LIFT1_DOWN         = 9
INDY_DO_ADDR_LIFT2_UP           = 10
INDY_DO_ADDR_LIFT2_DOWN         = 11
INDY_DO_ADDR_LIFT3_UP           = 12
INDY_DO_ADDR_LIFT3_DOWN         = 13
INDY_DO_ADDR_CLEAN_WATER_OPEN   = 14
INDY_DO_ADDR_CLEAN_AIR_OPEN     = 15
INDY_DO_ADDR_ICE_EXTRACT        = 16

JOB_PRIORITY_WAIT_POS       = 0
JOB_PRIORITY_REFRESH_MILK   = 1
JOB_PRIORITY_TRASH          = 2
JOB_PRIORITY_LIFT           = 3
JOB_PRIORITY_CLEAN          = 4
JOB_PRIORITY_ORDER_CHECK    = 5

def load_config() -> dict:
    data = {
        CONFIG_KEY_ROBOT_DOF: 6,
        CONFIG_KEY_DB_HOST: "192.168.137.11",
        CONFIG_KEY_DB_NAME: "KIOSK",
        CONFIG_KEY_DB_USER: "NEUROMEKA",
        CONFIG_KEY_DB_PWD: "NEUROMEKA1234",
        CONFIG_KEY_DB_TIMEOUT: 5,
        CONFIG_KEY_DB_LOGIN_TIMEOUT: 5,
        CONFIG_KEY_DB_CHARSET: 'utf8',
        CONFIG_KEY_ICE_ONLY: 4,
        CONFIG_KEY_WATER_ONLY: 0,
        CONFIG_KEY_ICE_AND_WATER: 1,
        CONFIG_KEY_COFFEE_MAP: {},
        CONFIG_KEY_COFFEE_EXPIRY_TIME: 600,
        CONFIG_KEY_CUP_DISP_PACKET_LEN: 11,
        CONFIG_KEY_ICE_DISP_PACKET_LEN: 5,
        CONFIG_KEY_MILK_REFRESH_DURATION: 4800,
        CONFIG_KEY_LIFT_DELAY: 10,
        CONFIG_KEY_LIFT_CUP_DELAY: 1,
        CONFIG_KEY_ESPRESSO_MACHINE_SHOT_DELAY_1: 6,
        CONFIG_KEY_ESPRESSO_MACHINE_SHOT_DELAY_2: 6,
        CONFIG_KEY_ESPRESSO_MACHINE_LONG_DELAY_1: 12,
        CONFIG_KEY_ESPRESSO_MACHINE_LONG_DELAY_2: 12,
    }
    try:
        with open(CONFIG_FILEPATH, "r") as f:
            new_data = yaml.load(f, Loader=yaml.FullLoader)
        data.update(new_data)
    except:
        save_config(data)
    return data


def save_config(data, no_retry=False):
    try:
        with open(CONFIG_FILEPATH, "w") as f:
            yaml.dump(data, f)
    except Exception as err:
        print(err)
        if no_retry:
            return
        os.remove(CONFIG_FILEPATH)
        save_config(data, True)
