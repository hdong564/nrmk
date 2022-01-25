# import dash_core_components as dcc
# import dash_bootstrap_components as dbc
# import dash_html_components as html
# from dash.dependencies import Input, Output

from indy.commander import *
from indy.indy_utils import indy_shm
# from App import app
# from Buttons import *
from status import *
from UI import *

def sig_handler(signum, frame):
    print('SIGNAL RECEIVED:', signum)
    GLOBAL_FLAG['run'] = False
    for th in thread_list:
        print("kill_thread")
        th.join()
    sys.exit(-1)


if __name__ == '__main__':
    import socket
    import signal, sys, os
    import threading
    import logging

    signal.signal(signal.SIGTERM, sig_handler) # shut down handling 
    signal.signal(signal.SIGINT, sig_handler)
# init start
# gotta find not run timing 
    GLOBAL_FLAG['run'] = True
    thread_list = []
    th0 = threading.Thread(target=app_ui) # run app_ui in thread 
    th0.start()
    thread_list.append(th0)

    th1 = threading.Thread(target=app_recipe_ui)
    th1.start()
    thread_list.append(th1)

    th2 = threading.Thread(target=commander)
    th2.start()
    thread_list.append(th2)

    th3 = threading.Thread(target=rt_status_update)
    th3.start()
    thread_list.append(th3)

    th4 = threading.Thread(target=safety_thread)
    th4.start()
    thread_list.append(th4)

    th5 = threading.Thread(target=data_logging)
    th5.start()
    thread_list.append(th5)

    def get_ipaddress():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        r = s.getsockname()[0]
        s.close()
        return r

    ip_addr = get_ipaddress()

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)