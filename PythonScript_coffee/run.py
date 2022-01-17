from Config import *
import signal, os, process_handler as ph, fcntl, sys, time
from indy_utils import indy_shm

INDY_HOME_JOINT_POSITION = [-88, 7, 105, 1, 66, 107]
INDY_HOME_BOUNDARY = 20

is_running = True
hProcess = ph.ProcessHandler()
lockfile = None

def sig_handler(signum, frame):
    print('SIGNAL RECEIVED:', signum)
    is_running = False
    hProcess.terminate()
    if lockfile is not None:
        lockfile.close()

def lift_up(shm):
    shm.set_do(INDY_DO_ADDR_LIFT1_UP, True)
    shm.set_do(INDY_DO_ADDR_LIFT2_UP, True)
    shm.set_do(INDY_DO_ADDR_LIFT3_UP, True)
    shm.set_do(INDY_DO_ADDR_LIFT1_DOWN, False)
    shm.set_do(INDY_DO_ADDR_LIFT2_DOWN, False)
    shm.set_do(INDY_DO_ADDR_LIFT3_DOWN, False)

def lift_down(shm):
    shm.set_do(INDY_DO_ADDR_LIFT1_UP, False)
    shm.set_do(INDY_DO_ADDR_LIFT2_UP, False)
    shm.set_do(INDY_DO_ADDR_LIFT3_UP, False)
    shm.set_do(INDY_DO_ADDR_LIFT1_DOWN, True)
    shm.set_do(INDY_DO_ADDR_LIFT2_DOWN, True)
    shm.set_do(INDY_DO_ADDR_LIFT3_DOWN, True)

def compare_home_position(cur_pos):
    passed = True
    for idx, angle in enumerate(cur_pos):
        diff = abs(angle - INDY_HOME_JOINT_POSITION[idx])
        if diff > INDY_HOME_BOUNDARY:
            passed = False
            break
    return passed

def recovery_lift(shm):
    lift_down(shm)
    
    print("Lift Down requested.")
    di_list = shm.get_di()
    while not (di_list[INDY_DI_ADDR_LIFT1_STATE_DOWN]\
        and di_list[INDY_DI_ADDR_LIFT2_STATE_DOWN]\
        and di_list[INDY_DI_ADDR_LIFT3_STATE_DOWN]):
        lift_down(shm)
        time.sleep(0.5)
        di_list = shm.get_di()
    
    print("Lift Up requested.")
    while not (di_list[INDY_DI_ADDR_LIFT1_STATE_UP]\
        and di_list[INDY_DI_ADDR_LIFT2_STATE_UP]\
        and di_list[INDY_DI_ADDR_LIFT3_STATE_UP]):
        if not di_list[INDY_DI_ADDR_HAND_PROTECTION]: # hand detected!
            lift_down(shm)
        else:
            lift_up(shm)
        time.sleep(0.05)
        di_list = shm.get_di()
    print("Lift recovery process done.")

if __name__ == "__main__":
    os.system("taskset -p -c 0,1 %d" % os.getpid())

    try:
        lockfile_name = "/tmp/coffee_automation_instance.lock"
        lockfile = open(lockfile_name, "w")
        fcntl.lockf(lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        # another instance is running or config load failed
        sys.exit(1)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    try:
        print("run.py initializing....")
        shm = indy_shm.IndyShmCommand(sync_mode=False)
        
        di_list = shm.get_di()
        print("Waiting for start button...")
        reset_btn_cnt = 0
        cmdbtn_cnt = 0
        cmd_timeout = 0
        redbtn_pushed = False
        moving_home = False

        shm.reset_robot()
        shm.stop_current_program()
        recovery_lift(shm)
        while is_running:
            di_list = shm.get_di()
            cur_pos = shm.get_joint_pos()

            if cmd_timeout > 0:
                cmd_timeout -= 1
            
            is_dt_mode = shm.get_robot_status()['direct_teaching']
            if di_list[INDY_DI_ADDR_BTN_RESET]:
                reset_btn_cnt += 1
                if not redbtn_pushed and not moving_home:
                    redbtn_pushed = True
                    cmd_timeout = 20
                    cmdbtn_cnt += 1
                if reset_btn_cnt >= 50 and not moving_home:
                    if is_dt_mode:
                        shm.direct_teaching(False)
                        time.sleep(0.2)
                    redbtn_pushed = False
                    cmd_timeout = 0
                    cmdbtn_cnt = 0
                    if not compare_home_position(cur_pos):
                        moving_home = True
                        time.sleep(0.5)
                        shm.joint_move_to(INDY_HOME_JOINT_POSITION)
                        time.sleep(0.5)
                        print("Start home motion.")
            else:
                redbtn_pushed = False
                if moving_home:
                    shm.stop_motion()
                    time.sleep(0.3)
                    shm.stop_current_program()
                    time.sleep(0.5)
                    shm.start_registered_default_program()
                    time.sleep(0.5)
                    shm.stop_current_program()
                    time.sleep(0.5)
                    moving_home = False
                    reset_btn_cnt = 0
                    print("Stopped home motion.")
                elif 0 < reset_btn_cnt < 50 and cmd_timeout == 0:
                    if cmdbtn_cnt == 5:
                        recovery_lift(shm)
                        raise "Force shutdown called."
                    elif cmdbtn_cnt == 10:
                        import subprocess
                        subprocess.call(["sudo", "reboot", "-h", "now"])
                        reset_btn_cnt = 0
                    elif cmdbtn_cnt == 3:
                        reset_btn_cnt = 0
                        shm.reset_robot()
                    else:
                        reset_btn_cnt = 0
                        shm.direct_teaching(not is_dt_mode)
                        print("Toggled direct teaching. State:", (not is_dt_mode))
                    cmd_timeout = 0
                    cmdbtn_cnt = 0
            
            if compare_home_position(cur_pos) and di_list[INDY_DI_ADDR_BTN_RUN_STATE]:
                break
            time.sleep(0.02)
            
        print("Start initiating program...")
        shm.reset_robot()

        while is_running and not shm.get_robot_status()['ready']:
            print("Waiting for robot state - Ready...")
            print(shm.get_robot_status())
            time.sleep(1)

        if shm.get_robot_status()['direct_teaching']:
            print("Trying to release direct teaching mode.")
            shm.direct_teaching(False)

        
        print("Starting default program...")
        shm.stop_current_program()
        time.sleep(1)
        shm.start_registered_default_program()
        time.sleep(1)
        while is_running and shm.get_program_state()['program_state'] != 'running':
            print("State:", shm.get_program_state()['program_state'])
            time.sleep(1)
        print("Starting default program...Done.")
    except Exception as e:
        print("Initialization fail:", e)
        lockfile.close()
        sys.exit(-1)
    
    hProcess.run(shm)

    try:
        shm.stop_current_program()
        recovery_lift(shm)
    finally:
        lockfile.close()
