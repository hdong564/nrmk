from status import *
if not GLOBAL_FLAG['test_mode']:
    print("TEST", GLOBAL_FLAG)
    from indy.indy_utils.indydcp_client import IndyDCPClient
    from indy.indy_utils.indy_shm import IndyShmCommand
    #from indy import LinearMotor as lm #no use
from indy.logic.recipe_logic import next_work
from indy.logic.commands import *

import json
# import time
from time import sleep, time
import signal, sys
import threading
import numpy as np
from datetime import datetime

import random


if not GLOBAL_FLAG['test_mode']:
    indy_master = IndyShmCommand()
    indy_master.set_sync_mode(True)
robot_connected = False
is_robot_initializing = False

COMMANDER_ADDR = 600  #B600 direct variables
EXTERNAL_TORQUE_EMERGENCY_THRESHOLD = list(abs(np.asarray([
    25,
    25,
    25,
    25,
    25,
    25
])))

SAFETY_PROGRAM_STOP_TICK = 0
CLEAR_RUNNING_COMMAND = False
COMMAND_CLEARED = False
IS_COMMAND_RUNNING = False
UI_REQUESTED_JOB = None

# all false in initial state
''' wait_for_initializing()
    set_job
    above two helper function for commander()
'''
def wait_for_initializing():
    global robot_connected, is_robot_initializing
    while GLOBAL_FLAG['run'] and (not robot_connected or is_robot_initializing):
        sleep(0.05)

def set_job(job):
    global CLEAR_RUNNING_COMMAND

    while GLOBAL_FLAG['run'] and not CLEAR_RUNNING_COMMAND and job.get_next_job() is not None:
        cmds = job.current_job
        STATUS_NEXT_WORK[0] = cmds.__repr__()
        
        cmds.start()
        for cmd in cmds.obtain_commands():
            if not GLOBAL_FLAG['test_mode']:
                while GLOBAL_FLAG['run'] and not CLEAR_RUNNING_COMMAND:
                    if (STATUS_ROBOT["system"] == 'ready'):
                        break
                    else:
                        sleep(0.1)
            if CLEAR_RUNNING_COMMAND:
                indy_master.write_direct_variable(0, COMMANDER_ADDR, 0)
                print("Command canceled.")
                return
            
            elif cmd.type == COMMAND_TYPE_STATUS:
                pos, status = cmd.params
                prev_status = STATUS_POS[pos]
                STATUS_POS[pos] = status
                print("CMD STATUS", pos, prev_status, "->", status)

            elif cmd.type == COMMAND_TYPE_COOKING_TIME:
                prev_time = STATUS_FRIED_TIME[cmds.pos]
                time = cmd.params
                if prev_time < 0:
                    time += prev_time
                    
                print("CMD COOKING_TIME", cmds.pos, prev_time, "->", f"{time} ({cmd.params})")
                STATUS_FRIED_TIME[cmds.pos] = time

            else: # cmd type: COMMAND_TYPE_LIMB
                print("CMD LIMB", cmd.params)
                if not GLOBAL_FLAG['test_mode']:
                    indy_master.write_direct_variable(0, COMMANDER_ADDR, cmd.params)
                    while GLOBAL_FLAG['run'] and not CLEAR_RUNNING_COMMAND:
                        #for handling potato machine
                        if len(POTATO_SIZE)>0:
                            start_extraction = time()
                            record_extraction = time()
                            while record_extraction < start_extraction + POTATO_EXTRACTION_TIMES[0]:
                                indy_master.set_do(DO_POTATO_EXTRACTION,True)
                                record_extraction = time() # update time 
                            indy_master.set_do(DO_POTATO_EXTRACTION,False)
                        if indy_master.read_direct_variable(0, COMMANDER_ADDR) == 0:
                            break
                        else:
                            sleep(0.05) #서버 응답용 통상 0.02~0.05s
                        '''wait until CLEAR_RUNNING_COMMAND done ?'''
                else:
                    sleep(1)
    
        cmds.done() 

def safety_thread():
    global SAFETY_PROGRAM_STOP_TICK, robot_connected, is_robot_initializing
    wait_for_initializing()
    while GLOBAL_FLAG['run'] and not GLOBAL_FLAG['test_mode']:
        #안전관련 코드 작성
        sleep(0.05)

def update_robot_state():
    status = indy_master.get_robot_status()
    for state in status.keys():
        if state == "movedone":
            continue
        if status[state]:
            if state == "busy":
                STATUS_ROBOT["system"] = "program_running"
            else:
                STATUS_ROBOT["system"] = state
    if STATUS_ROBOT["system"] == "home":
        STATUS_ROBOT["system"] = "ready"

def rt_status_update():
    global SAFETY_PROGRAM_STOP_TICK,\
        robot_connected,\
        CONTY_PROGRAM_IS_RUNNING,\
        UI_REQUESTED_JOB,\
        CLEAR_RUNNING_COMMAND,\
        COMMAND_CLEARED,\
        IS_COMMAND_RUNNING,\
        is_robot_initializing
    
    is_jog_moving = 0
    wait_for_initializing()
    prev_time = time()
    print("RT_STATUS start")    
    while GLOBAL_FLAG['run']:
        sleep(0.1)
        ui_request = STATUS_ROBOT["ui_request"] 
        if not GLOBAL_FLAG['test_mode']:
            # # 포토 센서
            di = indy_master.get_di()
            
            # 포토 센서 - 준비 공간
            if di[0] == False:
                if ('fried' in STATUS_POS['w0']):
                    STATUS_POS['w0'] = 'nothing'
                    FIN_EMPTY['w0'] = True
                WAITING_POINT['w0'] = 'empty'
            if di[0] == True:
                WAITING_POINT['w0'] = 'nothing'
            if di[1] == False:
                if ('fried' in STATUS_POS['w1']): # if done
                    STATUS_POS['w1'] = 'nothing'
                    FIN_EMPTY['w1'] = True
                WAITING_POINT['w1'] = 'empty'
            if di[1] == True:
                WAITING_POINT['w1'] = 'nothing'
            if di[2] == False:
                if ('fried' in STATUS_POS['w2']):
                    STATUS_POS['w2'] = 'nothing'
                    FIN_EMPTY['w2'] = True
                WAITING_POINT['w2'] = 'empty'
            if di[2] == True:
                WAITING_POINT['w2'] = 'nothing'
            if di[3] == False:
                if ('fried' in STATUS_POS['w3']):
                    STATUS_POS['w3'] = 'nothing'
                    FIN_EMPTY['w3'] = True
                WAITING_POINT['w3'] = 'empty'
            if di[3] == True:
                WAITING_POINT['w3'] = 'nothing'
            if di[4] == False:
                if ('fried' in STATUS_POS['w4']):
                    STATUS_POS['w4'] = 'nothing'
                    FIN_EMPTY['w4'] = True
                WAITING_POINT['w4'] = 'empty'
            if di[4] == True:
                WAITING_POINT['w4'] = 'nothing'
            if di[5] == False:
                if ('fried' in STATUS_POS['w5']):
                    STATUS_POS['w5'] = 'nothing'
                    FIN_EMPTY['w5'] = True
                WAITING_POINT['w5'] = 'empty'
            if di[5] == True:
                WAITING_POINT['w5'] = 'nothing'
            if di[6] == False:
                if ('fried' in STATUS_POS['w6']):
                    STATUS_POS['w6'] = 'nothing'
                    FIN_EMPTY['w6'] = True
                WAITING_POINT['w6'] = 'empty'
            if di[6] == True:
                WAITING_POINT['w6'] = 'nothing'
            if di[7] == False:
                if ('fried' in STATUS_POS['w7']):
                    STATUS_POS['w7'] = 'nothing'
                    FIN_EMPTY['w7'] = True
                WAITING_POINT['w7'] = 'empty'
            if di[7] == True:
                WAITING_POINT['w7'] = 'nothing'

            # WAITING_POINT['w0'] = 'empty' ###Test web
            # WAITING_POINT['w1'] = 'empty'
            # WAITING_POINT['w2'] = 'empty' ###Test web
            # WAITING_POINT['w3'] = 'empty'
            # WAITING_POINT['w4'] = 'nothing' ###Test web
            # WAITING_POINT['w5'] = 'nothing'
            # WAITING_POINT['w6'] = 'nothing' ###Test web
            # WAITING_POINT['w7'] = 'nothing'             
        
        if ui_request & UI_REQUEST_INIT_PROGRAM: #비트연산
            print("!! Init requested")
            CLEAR_RUNNING_COMMAND = True
            while GLOBAL_FLAG['run'] and not COMMAND_CLEARED:
                sleep(0.1)
            CLEAR_RUNNING_COMMAND = False
            STATUS_ROBOT["ui_request"] ^= UI_REQUEST_INIT_PROGRAM #XOR
            #현재 작업 모두 초기화
            for i in range(WAIT_NUM):
                STATUS_POS['w{}'.format(i)] = 'nothing'
            STATUS_ROBOT["holding"] = 'nothing'
            for i in range(FRY_NUM):
                STATUS_POS['f{}'.format(i)] = 'nothing'
                
            ORDER_LIST.clear()

            STATUS_FRIED_TIME['f0'] = 99999
            STATUS_FRIED_TIME['f1'] = 99999
            STATUS_FRIED_TIME['f2'] = 99999
            STATUS_FRIED_TIME['f3'] = 99999

            STATUS_NEXT_WORK = ['nothing']

            initialize()
            wait_for_initializing()           
                     
            continue
        
        if not GLOBAL_FLAG['test_mode']:
            # UI EndTool #10.26
            if (ui_request & UI_REQUEST_ENDT_ON):
                STATUS_ROBOT["ui_request"] ^= UI_REQUEST_ENDT_ON
                indy_master.set_endtool_do(0, 1)
            elif (ui_request & UI_REQUEST_ENDT_OFF):
                STATUS_ROBOT["ui_request"] ^= UI_REQUEST_ENDT_OFF
                indy_master.set_endtool_do(0, 0)
                #pass
        
        if is_robot_initializing:
            continue

        if robot_connected and not GLOBAL_FLAG['test_mode']:
            # UI CMD 실행
            if (ui_request & UI_REQUEST_CMD):
                STATUS_ROBOT["ui_request"] ^= UI_REQUEST_CMD
                cmd = STATUS_ROBOT["ui_cmd"]
                UI_REQUESTED_JOB = CommandJob().add_cmd(CMD_CUSTOM(COMMAND_TYPE_LIMB, cmd))

            # 프로그램 정지 토글 (UI 요청)
            prog_state = indy_master.get_program_state()['program_state']
            if (ui_request & UI_REQUEST_STOP):
                if prog_state != 'stop':
                    indy_master.stop_current_program()
                    indy_master.write_direct_variable(0, COMMANDER_ADDR, 0)
                    CLEAR_RUNNING_COMMAND = True
                    while GLOBAL_FLAG['run'] and not COMMAND_CLEARED:
                        sleep(0.1)
                    CLEAR_RUNNING_COMMAND = False
                    STATUS_ROBOT["system"] = 'paused'
                    for i in range(WAIT_NUM):
                        STATUS_POS['w{}'.format(i)] = 'nothing'
                    STATUS_ROBOT["holding"] = 'nothing'
            else:   
                # 일시정지 / 계속 진행
                if SAFETY_PROGRAM_STOP_TICK == 0:
                    if not (ui_request & UI_REQUEST_PAUSE):
                        # If not paused, update robot state
                        update_robot_state()

                    elif ui_request & UI_REQUEST_PAUSE and STATUS_ROBOT["system"] != 'paused':
                        print("!! Pause requested")
                        STATUS_ROBOT["system"] = 'paused'
                        indy_master.pause_current_program()
                    
                    elif ui_request & UI_REQUEST_RESUME:
                        print("!! Resume requested")
                        STATUS_ROBOT["ui_request"] ^= UI_REQUEST_RESUME
                        STATUS_ROBOT["ui_request"] ^= UI_REQUEST_PAUSE
                        STATUS_ROBOT["system"] = 'ready'
                        indy_master.resume_current_program()

        elif not GLOBAL_FLAG['test_mode']:
            STATUS_ROBOT["system"] = "not_ready"

        for i in range(FRY_NUM):  #시간계산 #상태 전환            
            pos = 'f{}'.format(i)
            status_pos = STATUS_POS[pos]
            if status_pos != 'nothing':
                recipe_num = int(status_pos[-2:])

                if 0 < recipe_num < 11: #음식종류 확인 (이전 코드수행시 걸린 시간처리)
                    STATUS_FRIED_TIME[pos] -= time()-prev_time
                    STATUS_FRIED_TIME_UI[pos] += time()-prev_time
                else:
                    STATUS_FRIED_TIME[pos] = 9999
                    STATUS_FRIED_TIME_UI[pos] = 0

                if STATUS_FRIED_TIME[pos] < 0:  #조리 시간 이후            
                    if ('notshaked1_' in status_pos):
                        STATUS_POS[pos] = 'waitshaking1_' + status_pos.replace("notshaked1_", "")                
                    elif ('shaked1_' in status_pos):
                        STATUS_POS[pos] = 'waitshaking2_' + status_pos.replace("shaked1_", "")
                    elif ('shaked2_' in status_pos):
                        STATUS_POS[pos] = 'waitshaking3_' + status_pos.replace("shaked2_", "")
                    elif ('shaked3_' in status_pos): #shaked 치킨
                        STATUS_POS[pos] = 'fried_' + status_pos.replace("shaked3_", "") 
                
                # if STATUS_FRIED_TIME[pos] < -50:
                #     print("'f{} overcooked {}".format(i, STATUS_FRIED_TIME[pos]))
                #####0518 추가 ## 흔들기 3 제거(일정시간흐른후)
                if ('waitshaking3_' in status_pos):
                    if STATUS_FRIED_TIME[pos] < -50:
                        STATUS_POS[pos] = 'fried_' + status_pos.replace("waitshaking3_", "") 
        
        prev_time = time()
    print("RT_STATUS end")

def initialize():
    global is_robot_initializing
    check_list = ['error', 'collision', 'emergency']
    is_robot_initializing = True
    
    if GLOBAL_FLAG['test_mode']:
        is_robot_initializing = False
        STATUS_ROBOT['system'] = 'ready'
        return
    
    #직접변수 초기화
    indy_master.write_direct_variable(0, COMMANDER_ADDR, 0)

    prog_state = indy_master.get_program_state()['program_state']
    ######
    robot_status = indy_master.get_robot_status()
    if robot_status['direct_teaching']:
        indy_master.direct_teaching(False)
        STATUS_ROBOT["direct_teaching"] = False

    # indy_master.stop_current_program()#####################################3
    reset_count = 0
    while GLOBAL_FLAG['run']:  #test2#
        robot_status = indy_master.get_robot_status()
        print("ROBOTSTATUS: Before reset",robot_status)
        if robot_status['resetting']:
            sleep(1)
            continue
        
        reset_required = False
        for chk in check_list:
            if robot_status[chk]:
                reset_required = True
                break
        if reset_required:
            print("Do reset!!")
            indy_master.reset_robot()
            if reset_count > 3:
                print("Do HARD reset!!")
                indy_master.reset_robot(hard_reset=True)
                exit(-1)
            reset_count += 1
        else:
            reset_count = 0
            break
        sleep(1)
    
    if (STATUS_ROBOT["ui_request"] & UI_REQUEST_GOHOME):
        STATUS_ROBOT["ui_request"] ^= UI_REQUEST_GOHOME

    direct_teaching_toggled = False
    pos_home = np.asarray(indy_master.get_joint_home())
    while GLOBAL_FLAG['run']: #직접교시 후 홈으로 이동할 수 있도록
        cur_pos = indy_master.get_joint_pos()
        ui_request = STATUS_ROBOT["ui_request"]
        diff = abs(pos_home - cur_pos)
        print(diff)
        diff = sum(diff) / 6
        if diff < 8:
            break
        else:
            robot_status = indy_master.get_robot_status()
            if (ui_request & UI_REQUEST_DT):
                if robot_status['direct_teaching']:
                    indy_master.direct_teaching(False)
                    STATUS_ROBOT["direct_teaching"] = False
                else:
                    indy_master.direct_teaching(True)
                    STATUS_ROBOT["direct_teaching"] = True
                STATUS_ROBOT["ui_request"] ^= UI_REQUEST_DT


            if (ui_request & UI_REQUEST_GOHOME):
                if robot_status['direct_teaching']:
                    indy_master.direct_teaching(False)
                    STATUS_ROBOT["direct_teaching"] = False

                indy_master.go_home()
                STATUS_ROBOT["ui_request"] ^= UI_REQUEST_GOHOME

            # UI EndTool#10.26
            # if (ui_request & UI_REQUEST_ENDT_ON):
            #     STATUS_ROBOT["ui_request"] ^= UI_REQUEST_ENDT_ON
            #     indy_master.set_endtool_do(0, 1)
            # elif (ui_request & UI_REQUEST_ENDT_OFF):
            #     STATUS_ROBOT["ui_request"] ^= UI_REQUEST_ENDT_OFF
            #     indy_master.set_endtool_do(0, 0)

        sleep(0.1)
    
    sleep(1)

    indy_master.go_home()
    if not GLOBAL_FLAG['run']:
        return
    
    # print("reset") ########################################################
    # indy_master.reset_robot()#############################################
    
    while GLOBAL_FLAG['run'] and STATUS_ROBOT['system'] != 'ready':
        update_robot_state()
        sleep(0.01)
    if not GLOBAL_FLAG['run']:
        return

    # indy_master.start_default_program()####################################
    # indy_master.start_current_program() ##test2#
    is_robot_initializing = False

def commander():
    global robot_connected, UI_REQUESTED_JOB, CLEAR_RUNNING_COMMAND, COMMAND_CLEARED, IS_COMMAND_RUNNING
    try:
        print("Commander Initializing")
        initialize()
        robot_connected = True
        print("Initializing_Finish")
        print("Commander Begin", "Global_FLAG[run] :", GLOBAL_FLAG['run'])
        while GLOBAL_FLAG['run']: # stuck in this block
            # print("Commander start")
            if CLEAR_RUNNING_COMMAND: #  false at initial state. if clear command triggered, get out of while loop
                COMMAND_CLEARED = True
                print("CMD - CLEAR_RUNNING_COMMAND:", CLEAR_RUNNING_COMMAND)
                sleep(0.1)
                continue
            
            COMMAND_CLEARED = False 
            ''' start main job'''
            work_class = next_work()
            work = work_class.GetWork()
            print("type of work::: ",type(work))

            ''' handle if there is no work'''
            if work is not None:
                print(f"[{STATUS_ROBOT['system']}] new job: {work.__repr__()}")
                #print(f"Work state: {work.get_next_job}")
            # decide which work todo.
            if work is None: # if there is no work, implement UI_requested work!!
                IS_COMMAND_RUNNING = False
                if UI_REQUESTED_JOB is None:
                    STATUS_NEXT_WORK[0] = 'nothing'
                else:
                    work = UI_REQUESTED_JOB
                    UI_REQUESTED_JOB = None
                    STATUS_NEXT_WORK[0] = work.__repr__()
                    set_job(work)
            else:
                # if there is work, set job of that work !!
                IS_COMMAND_RUNNING = True
                STATUS_NEXT_WORK[0] = work.__repr__()
                set_job(work)

            # print("Commander end")
            sleep(0.01)
    # except Exception as e:
    #     _, _ , tb = sys.exc_info() # tb -> traceback object
    #     print(sys.exc_info())
    #     print(f"file name = {__file__}")
    #     print(f'error line No = {tb.tb_lineno}')
    #     print(e)

    finally:
        robot_connected = False
        sleep(0.1)
        print("Commander Finish")

def data_logging():   

    while GLOBAL_FLAG['run']:
        if GLOBAL_FLAG['isChanged']:
            now = datetime.now()      
            data_log = open("/home/user/release/TasksDeployment/PythonScript/data_log_{}_{}_{}.txt".format(now.year,now.month,now.day), 'a')
            # data_log = open("data_log_{}_{}_{}.txt".format(now.year,now.month,now.day), 'a')
            print("data_log_open")
            # s = ",".join(ORDER_LIST)

            if GLOBAL_FLAG['menu_end1'] == True:
                pos = 'w0'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))                    
                    # data_log.write(s)            
                    END_COUNT['num'] += 1
                    CHECK_FLAG['menu_check1'] = True
                GLOBAL_FLAG['menu_end1'] = False
            
            if GLOBAL_FLAG['menu_end2'] == True:
                pos = 'w1'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)
                    END_COUNT['num'] += 1
                    CHECK_FLAG['menu_check2'] = True
                GLOBAL_FLAG['menu_end2'] = False

            if GLOBAL_FLAG['menu_end3'] == True:
                pos = 'w2'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)
                    END_COUNT['num'] += 1
                    CHECK_FLAG['menu_check3'] = True
                GLOBAL_FLAG['menu_end3'] = False

            if GLOBAL_FLAG['menu_end4'] == True:
                pos = 'w3'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)                    
                    END_COUNT['num'] += 1
                    CHECK_FLAG['menu_check4'] = True
                GLOBAL_FLAG['menu_end4'] = False

            if GLOBAL_FLAG['menu_end5'] == True:
                pos = 'w4'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)
                    CHECK_FLAG['menu_check5'] = True
                    END_COUNT['num'] += 1
                GLOBAL_FLAG['menu_end5'] = False

            if GLOBAL_FLAG['menu_end6'] == True:
                pos = 'w5'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)
                    CHECK_FLAG['menu_check6'] = True
                    END_COUNT['num'] += 1
                GLOBAL_FLAG['menu_end6'] = False

            if GLOBAL_FLAG['menu_end7'] == True:
                pos = 'w6'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)
                    CHECK_FLAG['menu_check7'] = True
                    END_COUNT['num'] += 1
                GLOBAL_FLAG['menu_end7'] = False
            
            if GLOBAL_FLAG['menu_end8'] == True:
                pos = 'w7'
                if ('fried' in STATUS_POS[pos]):
                    count = END_COUNT['num']
                    data_log.write('{} 제출 시간 : {}시{}분{}초, {} : fried_potato\n'.format(count,now.hour,now.minute,now.second,pos))
                    # data_log.write(s)
                    CHECK_FLAG['menu_check8'] = True
                    END_COUNT['num'] += 1
                GLOBAL_FLAG['menu_end8'] = False

            GLOBAL_FLAG['isChanged'] = False

            data_log.close()
        sleep(0.02)
