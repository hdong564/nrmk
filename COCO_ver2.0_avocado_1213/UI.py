from status import *
from time import sleep, time
from pyModbusTCP.client import ModbusClient
from indy.commander import *


from indy.indy_utils.indydcp_client import IndyDCPClient
from indy.indy_utils.indy_shm import IndyShmCommand

from indy.logic.chicken_logic import *
from indy.logic.commands import *

# indy_master = IndyShmCommand()
indy_master = IndyShmCommand(sync_mode=False)

work_start_time = time()

def app_ui():
    print("app_ui_client")    
    try:
        app_ui_client = ModbusClient(host=CB_IP, port=502) # CB ip : 192.168.0.52 , port 502
        print("app_ui_client", app_ui_client.is_open(), app_ui_client)

        while GLOBAL_FLAG['run']:
            if not app_ui_client.is_open():
                app_ui_client.open()
                #0으로 초기화
                for i in range(216):   
                    app_ui_client.write_multiple_registers(i, [0])
                print("app_ui_client open",app_ui_client.is_open())

            if app_ui_client.is_open():
                #로봇 상태 보내기
                if indy_master.get_robot_status()['ready'] == 1:
                    app_ui_client.write_multiple_registers(1, [4])

                elif indy_master.get_robot_status()['error'] == 1:
                    app_ui_client.write_multiple_registers(1, [3])

                elif indy_master.get_robot_status()['emergency'] == 1:
                    app_ui_client.write_multiple_registers(1, [2])
                
                else:
                    app_ui_client.write_multiple_registers(1, [1])

                #로봇 누적 작업 시간
                working_time = time()
                sec = int(working_time - work_start_time)

                hours = sec // 3600
                sec = sec - hours*3600
                mu = sec // 60
                # ss = sec - mu*60
                # print(hours, '시간', mu, '분', ss, '초 입니다.')

                app_ui_client.write_multiple_registers(2, [hours])
                app_ui_client.write_multiple_registers(3, [mu])

                #작업량
                app_ui_client.write_multiple_registers(4, [END_COUNT['num']])
                # print("작업량", END_COUNT['num'])
                
                #로봇 현재 작업 종류
                if STATUS_ROBOT["working"] == 0:
                    app_ui_client.write_multiple_registers(5, [0])
                elif (STATUS_ROBOT["working"] == 1):
                    app_ui_client.write_multiple_registers(5, [1])
                elif (STATUS_ROBOT["working"] == 2):
                    app_ui_client.write_multiple_registers(5, [2])
                elif (STATUS_ROBOT["working"] == 3):
                    app_ui_client.write_multiple_registers(5, [3])

                #튀김기 레시피 상태

                # mod bus 
                # M006 ~ 9 
                # 1 if shaking
                # 0 if waiting
                # n for doing nth recipe
                for i in range(4):
                    f_pos = 'f{}'.format(i)
                    status_f_pos = STATUS_POS[f_pos]
                    if status_f_pos == 'nothing':
                        app_ui_client.write_multiple_registers(6+i, [0])
                    else:
                        for j in range(11):
                            if int(status_f_pos[-2:]) == j:
                                app_ui_client.write_multiple_registers(6+i, [j])

                #튀김기 조리시간 (시간, 분)
                def sec2sec(sec):
                    if sec > 0 :
                        return int(sec%60)
                    else: 
                        return int(sec%-60)

                def sec2min(sec):
                    if sec > 0 :
                        return int(sec/60)
                    else: 
                        return int(sec/60)
 
                #분
                app_ui_client.write_multiple_registers(14, [sec2min(STATUS_FRIED_TIME_UI["f0"])])
                app_ui_client.write_multiple_registers(15, [sec2min(STATUS_FRIED_TIME_UI["f1"])])
                app_ui_client.write_multiple_registers(16, [sec2min(STATUS_FRIED_TIME_UI["f2"])])
                app_ui_client.write_multiple_registers(17, [sec2min(STATUS_FRIED_TIME_UI["f3"])])
                #초
                app_ui_client.write_multiple_registers(18, [sec2sec(STATUS_FRIED_TIME_UI["f0"])])
                app_ui_client.write_multiple_registers(19, [sec2sec(STATUS_FRIED_TIME_UI["f1"])])
                app_ui_client.write_multiple_registers(20, [sec2sec(STATUS_FRIED_TIME_UI["f2"])])
                app_ui_client.write_multiple_registers(21, [sec2sec(STATUS_FRIED_TIME_UI["f3"])])         
                
                #튀김기 조리 종료 팝업 신호

                # key 22 reg value 1 then it is done ! if done, make it wait status 
                if app_ui_client.read_holding_registers(22, 1)[0] == 1:
                    if STATUS_POS["f0"] == 'nothing':
                        app_ui_client.write_multiple_registers(22, [0])

                    else:
                        STATUS_POS[ "f0"] = 'fried_' + STATUS_POS["f0"][-2:]
                        EARLY_FIN["f0"] = True

                if app_ui_client.read_holding_registers(23, 1)[0] == 1:
                    if STATUS_POS["f1"] == 'nothing':
                        app_ui_client.write_multiple_registers(23, [0])

                    else:
                        STATUS_POS["f1"] = 'fried_' + STATUS_POS["f1"][-2:]
                        EARLY_FIN["f1"] = True
                
                if app_ui_client.read_holding_registers(24, 1)[0] == 1:
                    if STATUS_POS["f2"] == 'nothing':
                        app_ui_client.write_multiple_registers(24, [0])

                    else:
                        STATUS_POS["f2"] = 'fried_' + STATUS_POS["f2"][-2:]
                        EARLY_FIN["f2"] = True

                if app_ui_client.read_holding_registers(25, 1)[0] == 1:
                    if STATUS_POS["f3"] == 'nothing':
                        app_ui_client.write_multiple_registers(25, [0])

                    else:
                        STATUS_POS["f3"] = 'fried_' + STATUS_POS["f3"][-2:]
                        EARLY_FIN                                    

                #바스켓 레시피 선택시 레시피 신호
                for i in range(8):
                    w_pos = f'w{i}' # set wi 
                    if app_ui_client.read_holding_registers(52+i, 1)[0] == 1: # read 1 byte of holding registers
                        if 0 < app_ui_client.read_holding_registers(34+i, 1)[0] < 11: #레시피 1~10
                            #레시피 조리시간 확인 예외처리
                            recipe_num = app_ui_client.read_holding_registers(34+i, 1)[0] # reading recipe status 
                            if (RECIPE_DATA_APP[recipe_num-1][0] == 0) and (RECIPE_DATA_APP[recipe_num-1][1] == 0):
                                print("레시피 에러 - 조리시간이 0", w_pos)
                            else:   #recipe num of each basket goto status_pos -> repr, making recipe... 
                                if app_ui_client.read_holding_registers(34+i, 1)[0] > 9:
                                    # recipe 10 case -> [-2:] able
                                    STATUS_POS[w_pos] = str(app_ui_client.read_holding_registers(34+i, 1)[0]) 
                                else: #recipe smaller than 10 case -> one digit decimal -> need '0' string 
                                    STATUS_POS[w_pos] = '0' + str(app_ui_client.read_holding_registers(34+i, 1)[0])
                                # app_ui_client.write_multiple_registers(34+i, [0])
                                app_ui_client.write_multiple_registers(26+i, [1])
                                app_ui_client.write_multiple_registers(52+i, [0])
                                ORDER_LIST.append(w_pos)
                            # print("레시피",w_pos,STATUS_POS[w_pos])

                #바스켓 상태
                # if (WAITING_POINT['w0'] == 'nothing') and ('frying' in STATUS_POS['w0']): #조리전
                #     app_ui_client.write_multiple_registers(26, [1]) 
                # elif (WAITING_POINT['w0'] == 'nothing') and ('fried' in STATUS_POS['w0']):  #조리 완료
                #     app_ui_client.write_multiple_registers(26, [2])
                # elif WAITING_POINT['w0'] == 'empty': #없음
                #     app_ui_client.write_multiple_registers(26, [0])
                for i in range(8):
                    w_pos = 'w{}'.format(i)
                    if WAITING_POINT[w_pos] == 'empty': #없음
                        app_ui_client.write_multiple_registers(26+i, [0])
                    elif (WAITING_POINT[w_pos] == 'nothing') and ('fried' not in STATUS_POS[w_pos]): #조리전
                        if (app_ui_client.read_holding_registers(26+i, 1)[0] != 3):
                            app_ui_client.write_multiple_registers(26+i, [1]) #조리 전
                    elif (WAITING_POINT[w_pos] == 'nothing') and ('fried' in STATUS_POS[w_pos]):  #조리 완료
                        app_ui_client.write_multiple_registers(26+i, [2])#조리 완료                        
                        # app_ui_client.write_multiple_registers(34+i, [0]) #바스켓 레시피 초기화 신호
                
                #직접교시 on/off
                if app_ui_client.read_holding_registers(42, 1)[0] == 1:
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        # print("직접교시 on")
                        # STATUS_ROBOT["ui_request"] |= UI_REQUEST_DT
                        indy_master.direct_teaching(True)
                    app_ui_client.write_multiple_registers(42, [0])
                    app_ui_client.write_multiple_registers(210, [1])   
                elif app_ui_client.read_holding_registers(42, 1)[0] == 2:
                    # print("직접교시 off")
                    # STATUS_ROBOT["ui_request"] |= UI_REQUEST_DT                    
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        indy_master.direct_teaching(False)
                    app_ui_client.write_multiple_registers(42, [0])
                    app_ui_client.write_multiple_registers(210, [2])                 

                #그리퍼 on/off
                if app_ui_client.read_holding_registers(43, 1)[0] == 1:
                    # print("그리퍼 on")                    
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        STATUS_ROBOT["ui_request"] |= UI_REQUEST_ENDT_ON 
                    app_ui_client.write_multiple_registers(43, [0])
                    app_ui_client.write_multiple_registers(211, [1])  
                elif app_ui_client.read_holding_registers(43, 1)[0] == 2:
                    # print("그리퍼 off")                    
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        STATUS_ROBOT["ui_request"] |= UI_REQUEST_ENDT_OFF
                    app_ui_client.write_multiple_registers(43, [0])
                    app_ui_client.write_multiple_registers(211, [2])  

                #로봇 초기화 on
                if app_ui_client.read_holding_registers(44, 1)[0] == 1:
                    print("초기화 on")
                    STATUS_ROBOT["ui_request"] |= UI_REQUEST_INIT_PROGRAM
                    for i in range(8):
                        app_ui_client.write_multiple_registers(34+i, [0])
                    app_ui_client.write_multiple_registers(44, [0])

                #default 프로그램 제어
                if app_ui_client.read_holding_registers(45, 1)[0] == 1:
                    print("dafault start")
                    indy_master.set_prog_ratio(1.0)
                    indy_master.set_cmd_ratio(1.0)
                    indy_master.start_default_program()
                    # indy_master.start_current_program()
                    app_ui_client.write_multiple_registers(45, [0])
                    app_ui_client.write_multiple_registers(212, [1])
                elif app_ui_client.read_holding_registers(45, 1)[0] == 2:
                    print("dafault resume")
                    indy_master.set_prog_ratio(1.0)
                    indy_master.set_cmd_ratio(1.0)
                    indy_master.resume_current_program()
                    # STATUS_ROBOT["ui_request"] |= UI_REQUEST_RESUME
                    app_ui_client.write_multiple_registers(45, [0])
                    app_ui_client.write_multiple_registers(212, [2])  
                elif app_ui_client.read_holding_registers(45, 1)[0] == 3:
                    print("dafault pause")
                    indy_master.pause_current_program()
                    # STATUS_ROBOT["ui_request"] |= UI_REQUEST_PAUSE
                    app_ui_client.write_multiple_registers(45, [0])
                    app_ui_client.write_multiple_registers(212, [3])  
                elif app_ui_client.read_holding_registers(45, 1)[0] == 4:
                    print("dafault stop")
                    indy_master.stop_current_program()
                    app_ui_client.write_multiple_registers(45, [0])
                    app_ui_client.write_multiple_registers(212, [4])  

                #홈자세 이동
                if app_ui_client.read_holding_registers(46, 1)[0] == 1:
                    indy_master.set_prog_ratio(1.0)
                    indy_master.set_cmd_ratio(1.0)                    
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        indy_master.go_home()
                    app_ui_client.write_multiple_registers(49, [1])
                    app_ui_client.write_multiple_registers(213, [1])  
                elif app_ui_client.read_holding_registers(46, 1)[0] == 0:
                    app_ui_client.write_multiple_registers(213, [0])  
                    if app_ui_client.read_holding_registers(49, 1)[0] == 1:                        
                        if indy_master.get_program_state()['program_state'] == 'stop':
                          indy_master.stop_motion()
                        app_ui_client.write_multiple_registers(49, [0])

                #제로자세 이동
                if app_ui_client.read_holding_registers(47, 1)[0] == 1:
                    indy_master.set_prog_ratio(1.0)
                    indy_master.set_cmd_ratio(1.0)                    
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        indy_master.go_zero()
                    app_ui_client.write_multiple_registers(50, [1])
                    app_ui_client.write_multiple_registers(214, [1])  
                elif app_ui_client.read_holding_registers(47, 1)[0] == 0:
                    app_ui_client.write_multiple_registers(214, [0])  
                    if app_ui_client.read_holding_registers(50, 1)[0] == 1:                        
                        if indy_master.get_program_state()['program_state'] == 'stop':
                           indy_master.stop_motion()
                        app_ui_client.write_multiple_registers(50, [0])              

                #포장자세 이동
                #미구현
                if app_ui_client.read_holding_registers(48, 1)[0] == 1:
                    indy_master.set_prog_ratio(1.0)
                    indy_master.set_cmd_ratio(1.0)                    
                    if indy_master.get_program_state()['program_state'] == 'stop':
                        indy_master.joint_move_to([90,0,-150,5,150,0])
                    app_ui_client.write_multiple_registers(51, [1])
                    app_ui_client.write_multiple_registers(215, [1])  
                elif app_ui_client.read_holding_registers(48, 1)[0] == 0:
                    app_ui_client.write_multiple_registers(215, [0])  
                    if app_ui_client.read_holding_registers(51, 1)[0] == 1:                        
                        if indy_master.get_program_state()['program_state'] == 'stop':
                         indy_master.stop_motion()
                        app_ui_client.write_multiple_registers(51, [0]) 

                #로봇 충돌 리셋
                if app_ui_client.read_holding_registers(216, 1)[0] == 1:
                    print("충돌초기화 on")
                    indy_master.reset_robot()
                    app_ui_client.write_multiple_registers(216, [0])

                #로봇 메뉴 취소
                if app_ui_client.read_holding_registers(217, 1)[0] != 0:
                    basket_num = app_ui_client.read_holding_registers(217, 1)[0] - 1
                    if basket_num >= 0:
                        w_pos = 'w{}'.format(basket_num)                    
                        print("메뉴취소")
                        if len(ORDER_LIST):
                            ORDER_LIST.remove(w_pos)
                            STATUS_POS[w_pos] = 'nothing'
                    app_ui_client.write_multiple_registers(217, [0])

                #레시피 초기화
                for i in range(8):
                    w_pos = 'w{}'.format(i)
                    if FIN_EMPTY[w_pos] == True:  #초기화 필요
                        app_ui_client.write_multiple_registers(34+i, [0])
                        FIN_EMPTY[w_pos] = False

                # ########################
                # print('#################################')
                # print(app_ui_client.read_holding_registers(6, 1)[0])
                # print(app_ui_client.read_holding_registers(7, 1)[0])
                # print(app_ui_client.read_holding_registers(8, 1)[0])
                # print(app_ui_client.read_holding_registers(9, 1)[0])
                # # print(app_ui_client.read_holding_registers(38, 1)[0])
                # # print(app_ui_client.read_holding_registers(39, 1)[0])
                # # print(app_ui_client.read_holding_registers(40, 1)[0])
                # # print(app_ui_client.read_holding_registers(41, 1)[0])
                # print('------------------------------')
                # print(app_ui_client.read_holding_registers(14, 1)[0])
                # print(app_ui_client.read_holding_registers(18, 1)[0])
                # print(app_ui_client.read_holding_registers(15, 1)[0])
                # print(app_ui_client.read_holding_registers(19, 1)[0])
                # print(app_ui_client.read_holding_registers(16, 1)[0])
                # print(app_ui_client.read_holding_registers(20, 1)[0])
                # print(app_ui_client.read_holding_registers(17, 1)[0])
                # print(app_ui_client.read_holding_registers(21, 1)[0])
                # # print(app_ui_client.read_holding_registers(83, 1)[0])
                # # print(app_ui_client.read_holding_registers(84, 1)[0])
                # # print(app_ui_client.read_holding_registers(85, 1)[0])
                # # print(app_ui_client.read_holding_registers(86, 1)[0])
                # # print(app_ui_client.read_holding_registers(87, 1)[0])
                # # print(app_ui_client.read_holding_registers(88, 1)[0])
                # # print(app_ui_client.read_holding_registers(89, 1)[0])
                # print('#################################')
                # print(app_ui_client.read_holding_registers(42, 1)[0])
                # print(app_ui_client.read_holding_registers(43, 1)[0])
                # print(app_ui_client.read_holding_registers(44, 1)[0])
                # print(app_ui_client.read_holding_registers(45, 1)[0])
                # print(app_ui_client.read_holding_registers(46, 1)[0])
                # print(app_ui_client.read_holding_registers(47, 1)[0])
                # print('#################################')          

            sleep(0.05)            

    finally:
        sleep(0.05)
        app_ui_client.close()
        print("app_ui_thread close")

def app_recipe_ui():
    print("app_recipe_ui_client")    
    try:
        app_recipe_ui_client = ModbusClient(host=CB_IP, port=502)
        print("app_recipe_ui_client", app_recipe_ui_client.is_open(), app_recipe_ui_client)

        while GLOBAL_FLAG['run']:
            if not app_recipe_ui_client.is_open():
                app_recipe_ui_client.open()
                print("app_recipe_ui_client open",app_recipe_ui_client.is_open())

            if app_recipe_ui_client.is_open():
                #레시피 세팅
                #레시피 정보
                for i in range(10):
                    for j in range(15):
                        RECIPE_DATA_APP[i][j] = app_recipe_ui_client.read_holding_registers(60+15*i+j, 1)[0]

                        #레시피 세팅
                        #각각 시간 파악
                        if (RECIPE_DATA_APP[i][2] + RECIPE_DATA_APP[i][6] + RECIPE_DATA_APP[i][10] == 0):#흔들기 없는 경우
                            RECIPE_DATA_APP[i][18] = RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1]  #shaked3 조리시간

                        elif (RECIPE_DATA_APP[i][2] + RECIPE_DATA_APP[i][6] + RECIPE_DATA_APP[i][10] == 1):#흔들기 1회
                            if (RECIPE_DATA_APP[i][4] == 0) and (RECIPE_DATA_APP[i][5] == 0):#흔들기 1회 바로하는 경우
                                RECIPE_DATA_APP[i][18] = RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1]  #shaked3                            
                            else: #흔들기 1회 나중에 하는 경우                        
                                RECIPE_DATA_APP[i][15] = RECIPE_DATA_APP[i][4]*60 + RECIPE_DATA_APP[i][5] #notshaked1
                                RECIPE_DATA_APP[i][18] =  RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1] - RECIPE_DATA_APP[i][15] #shaked3
                        
                        elif (RECIPE_DATA_APP[i][2] + RECIPE_DATA_APP[i][6] + RECIPE_DATA_APP[i][10] == 2):#흔들기 2회
                            if (RECIPE_DATA_APP[i][4] == 0) and (RECIPE_DATA_APP[i][5] == 0):#흔들기 1회 바로하는 경우
                                RECIPE_DATA_APP[i][17] = RECIPE_DATA_APP[i][8]*60 + RECIPE_DATA_APP[i][9]    #shaked2
                                RECIPE_DATA_APP[i][18] = RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1] - RECIPE_DATA_APP[i][17]  #shaked3                            
                            else: #흔들기 1회 나중에 하는 경우
                                RECIPE_DATA_APP[i][15] = RECIPE_DATA_APP[i][4]*60 + RECIPE_DATA_APP[i][5]    #notshaked1
                                RECIPE_DATA_APP[i][17] = RECIPE_DATA_APP[i][8]*60 + RECIPE_DATA_APP[i][9] - RECIPE_DATA_APP[i][15]    #shaked2 
                                RECIPE_DATA_APP[i][18] = RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1] - RECIPE_DATA_APP[i][17] - RECIPE_DATA_APP[i][15]  #shaked3
                        
                        elif (RECIPE_DATA_APP[i][2] + RECIPE_DATA_APP[i][6] + RECIPE_DATA_APP[i][10] == 3):#흔들기 3회
                            if (RECIPE_DATA_APP[i][4] == 0) and (RECIPE_DATA_APP[i][5] == 0):#흔들기 1회 바로하는 경우
                                RECIPE_DATA_APP[i][16] = RECIPE_DATA_APP[i][8]*60 + RECIPE_DATA_APP[i][9]    #shaked1
                                RECIPE_DATA_APP[i][17] = RECIPE_DATA_APP[i][12]*60 + RECIPE_DATA_APP[i][13] - RECIPE_DATA_APP[i][16]   #shaked2 
                                RECIPE_DATA_APP[i][18] = RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1] - RECIPE_DATA_APP[i][16] - RECIPE_DATA_APP[i][17]  #shaked3
                            
                            else: #흔들기 1회 나중에 하는 경우 
                                RECIPE_DATA_APP[i][15] = RECIPE_DATA_APP[i][4]*60 + RECIPE_DATA_APP[i][5]    #notshaked1
                                RECIPE_DATA_APP[i][16] = RECIPE_DATA_APP[i][8]*60 + RECIPE_DATA_APP[i][9] - RECIPE_DATA_APP[i][15]     #shaked1
                                RECIPE_DATA_APP[i][17] = RECIPE_DATA_APP[i][12]*60 + RECIPE_DATA_APP[i][13] - RECIPE_DATA_APP[i][15] - RECIPE_DATA_APP[i][16]    #shaked2 
                                RECIPE_DATA_APP[i][18] = RECIPE_DATA_APP[i][0]*60 + RECIPE_DATA_APP[i][1] - RECIPE_DATA_APP[i][15] - RECIPE_DATA_APP[i][16] - RECIPE_DATA_APP[i][17] #shaked3
                
            sleep(0.1)            

    finally:
        sleep(0.1)
        app_recipe_ui_client.close()
        print("app_recipe_ui_client_thread close")


if __name__ == '__main__':
    import threading
    th0 = threading.Thread(target=app_ui)
    th0.start()

    th1 = threading.Thread(target=app_recipe_ui)
    th1.start()