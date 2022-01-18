

from time import time
from time import sleep
from indy.logic.commands import *
from status import *

def custom_done_callback(self):
    STATUS_ROBOT["holding"] = STATUS_POS[self.pos]
    STATUS_POS[self.pos] = "nothing"

def next_work():
    todo = {}
    #우선순위 추가시 추가필요
    for i in range(3):
        todo[i] = []

    usable_place_num = [i for i in range(FRY_NUM) if STATUS_POS_USABLE['f{}'.format(i)]]

    for i in usable_place_num:
        f_pos = 'f{}'.format(i)
        status_f_pos = STATUS_POS[f_pos]
        if status_f_pos != 'nothing':

            recipe_num = int(status_f_pos[-2:])

            # 0 순위 작업 #fry끝난거 먼저
            if ('fried' in status_f_pos):  #fin cooking
                if (STATUS_FRIED_TIME_UI[f_pos] > (RECIPE_DATA_APP[recipe_num-1][0]*60 + RECIPE_DATA_APP[recipe_num-1][1])) or (EARLY_FIN[f_pos] == True):
                    cmd = CommandJob()
                    cmd.clear_commands()
                    cmd.add_cmd(CMD_FRY_PICKUP(f_pos, 10)) #pickup time
                    cmd.add_cmd(CMD_AIR_SHAKE(f_pos))

                    #원래 waiting point 위치로 
                    # if (STATUS_POS[PREV_POS_DATA[f_pos]] == 'nothing'):                
                    cmd.add_cmd(CMD_WAIT_PLACE(PREV_POS_DATA[f_pos], 10, f_pos)).set_cooking_pos(f_pos)
                    print("Fry fin pos->", PREV_POS_DATA[f_pos]) #test
                    # STATUS_FRIED_TIME_UI[f_pos] = 0
                    EARLY_FIN[f_pos] = False
                    todo[0].append(cmd)

            if ('waitshaking1' in status_f_pos): #흔들기 유무에 따라
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 1):#흔들기 1회
                    cmd = CommandJob()
                    cmd.clear_commands()
                    status = "shaked3_" + status_f_pos.replace("waitshaking1_", "") #상태 바뀜
                    cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
                    cmd.set_cooking_pos(f_pos)
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
                    todo[2].append(cmd)
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 2):#흔들기 2회
                    cmd = CommandJob()
                    cmd.clear_commands()
                    status = "shaked2_" + status_f_pos.replace("waitshaking1_", "") #상태 바뀜
                    cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
                    cmd.set_cooking_pos(f_pos)
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
                    todo[2].append(cmd)
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    # 1순위
                    cmd = CommandJob()
                    cmd.clear_commands()
                    status = "shaked1_" + status_f_pos.replace("waitshaking1_", "") #상태 바뀜
                    cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
                    cmd.set_cooking_pos(f_pos)
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
                    todo[2].append(cmd)            
            
            if ('waitshaking2' in status_f_pos):            
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 2):#흔들기 2회
                    cmd = CommandJob()
                    cmd.clear_commands()
                    status = "shaked3_" + status_f_pos.replace("waitshaking2_", "") #상태 바뀜
                    cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
                    cmd.set_cooking_pos(f_pos)
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
                    todo[2].append(cmd)
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    cmd = CommandJob()
                    cmd.clear_commands()
                    status = "shaked2_" + status_f_pos.replace("waitshaking2_", "") #상태 바뀜
                    cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
                    cmd.set_cooking_pos(f_pos)
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
                    todo[2].append(cmd)

            if ('waitshaking3' in status_f_pos):
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    cmd = CommandJob()
                    status = "shaked3_" + status_f_pos.replace("waitshaking3_", "") #상태 바뀜
                    cmd.add_cmd(CMD_FRY_PICKUP_N_SHAKE(f_pos, 10))
                    cmd.set_cooking_pos(f_pos)
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos))
                    todo[2].append(cmd)
        
        # 2 순위 작업
    if len(ORDER_LIST) and (todo[0] == []):
        print("##################################################")
        print(ORDER_LIST)
        # print(WAITING_POINT(ORDER_LIST[0]))
        print("##################################################")
        w_pos = ORDER_LIST[0]    #포토센서 보고 작업하기 WAITING_POINT  #commander에서 유무 판단
        # WAITING_POINT['w0'] = 'empty' ###Test web
        # WAITING_POINT['w1'] = 'empty'
        # WAITING_POINT['w2'] = 'empty' ###Test web
        # WAITING_POINT['w3'] = 'empty'
        # WAITING_POINT['w4'] = 'nothing' ###Test web
        # WAITING_POINT['w5'] = 'nothing'
        # WAITING_POINT['w6'] = 'nothing' ###Test web
        # WAITING_POINT['w7'] = 'nothing'        

        if STATUS_POS[w_pos] != 'nothing':
            recipe_num = int(STATUS_POS[w_pos][-2:])
        else:
            recipe_num = 0
        #################ZONE별로 다른 프라이에##############set1
        if (w_pos == 'w0') or (w_pos == 'w2'):
            f_pos = 'f0'
            print("using fry 1") ##debug용
            if (0 < recipe_num < 11) and (STATUS_POS[f_pos] == 'nothing') and (WAITING_POINT[w_pos] == 'nothing'): #wait에 음식 ---> fry에 튀기기 #위치저장
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 0):#흔들기 없는 경우
                    status = "shaked3_" + STATUS_POS[w_pos]
                    cmd = CommandJob()
                    cmd.clear_commands()
                    cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                    cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.set_cooking_pos(f_pos)
                    PREV_POS_DATA[f_pos] = w_pos

                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 1):#흔들기 1회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked3_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 2):#흔들기 2회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked2_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                    
                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                print("Fry start pos->", f_pos,w_pos) #test
                del ORDER_LIST[0]
                todo[1].append(cmd)

            else:
                del ORDER_LIST[0]
                ORDER_LIST.append(w_pos)        

        elif (w_pos == 'w1') or (w_pos == 'w3'):
            f_pos = 'f1'
            print("using fry 2") ##debug용
            if (0 < recipe_num < 11) and (STATUS_POS[f_pos] == 'nothing') and (WAITING_POINT[w_pos] == 'nothing'): #wait에 음식 ---> fry에 튀기기 #위치저장
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 0):#흔들기 없는 경우
                    status = "shaked3_" + STATUS_POS[w_pos]
                    cmd = CommandJob()
                    cmd.clear_commands()
                    cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                    cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.set_cooking_pos(f_pos)
                    PREV_POS_DATA[f_pos] = w_pos

                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 1):#흔들기 1회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked3_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 2):#흔들기 2회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked2_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                    
                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                print("Fry start pos->", f_pos,w_pos) #test
                del ORDER_LIST[0]                   
                todo[1].append(cmd)

            else:
                del ORDER_LIST[0]
                ORDER_LIST.append(w_pos) 
            ###################################set2
        elif (w_pos == 'w4') or (w_pos == 'w6'):
            f_pos = 'f2'
            print("using fry 3") ##debug용
            if (0 < recipe_num < 11) and (STATUS_POS[f_pos] == 'nothing') and (WAITING_POINT[w_pos] == 'nothing'): #wait에 음식 ---> fry에 튀기기 #위치저장
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 0):#흔들기 없는 경우
                    status = "shaked3_" + STATUS_POS[w_pos]
                    cmd = CommandJob()
                    cmd.clear_commands()
                    cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                    cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.set_cooking_pos(f_pos)
                    PREV_POS_DATA[f_pos] = w_pos

                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 1):#흔들기 1회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked3_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 2):#흔들기 2회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked2_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                    
                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                print("Fry start pos->", f_pos,w_pos) #test
                del ORDER_LIST[0]                   
                todo[1].append(cmd)

            else:
                del ORDER_LIST[0]
                ORDER_LIST.append(w_pos)         

        elif (w_pos == 'w5') or (w_pos == 'w7'):
            f_pos = 'f3'
            print("using fry 4") ##debug용
            if (0 < recipe_num < 11) and (STATUS_POS[f_pos] == 'nothing') and (WAITING_POINT[w_pos] == 'nothing'): #wait에 음식 ---> fry에 튀기기 #위치저장
                if (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 0):#흔들기 없는 경우
                    status = "shaked3_" + STATUS_POS[w_pos]
                    cmd = CommandJob()
                    cmd.clear_commands()
                    cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                    cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                    cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                    cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                    cmd.set_cooking_pos(f_pos)
                    PREV_POS_DATA[f_pos] = w_pos

                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 1):#흔들기 1회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked3_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 2):#흔들기 2회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked2_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                
                elif (RECIPE_DATA_APP[recipe_num-1][2] + RECIPE_DATA_APP[recipe_num-1][6] + RECIPE_DATA_APP[recipe_num-1][10] == 3):#흔들기 3회
                    if (RECIPE_DATA_APP[recipe_num-1][4] == 0) and (RECIPE_DATA_APP[recipe_num-1][5] == 0):#흔들기 1회 바로하는 경우
                        status = "shaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos
                    
                    else: #흔들기 1회 나중에 하는 경우
                        status = "notshaked1_" + STATUS_POS[w_pos]
                        cmd = CommandJob()
                        cmd.clear_commands()
                        cmd.add_cmd(CMD_WAIT_PICKUP(w_pos, 10))
                        cmd.add_cmd(CMD_FRY_PLACE_SHAKENONE(f_pos, 10))
                        cmd.add_cmd(CMD_SET_COOKING_TIME(f_pos, time=get_frying_time(status)))
                        cmd.add_cmd(CMD_CHANGE_STATUS(f_pos, status))
                        cmd.set_cooking_pos(f_pos)
                        PREV_POS_DATA[f_pos] = w_pos

                print("Fry start pos->", f_pos,w_pos) #test
                del ORDER_LIST[0]                   
                todo[1].append(cmd)

            else:
                del ORDER_LIST[0]
                ORDER_LIST.append(w_pos)                    

    # 다음 작업 결정 
    if todo[0]:
        for work in todo[0]:
            return work           
    
    elif todo[1]:
        for work in todo[1]:
            return work 

    elif todo[2]:
        for work in todo[2]:
            return work 

    elif (todo[0] == []) and (todo[1] == []) and (todo[2] == []):
        cmd = CommandJob()
        cmd.clear_commands()
        cmd.add_cmd(CMD_WAIT_CMD())
        work = cmd
        return work  
            
    return None