# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import dash_bootstrap_components as dbc

# from App import app
# from Buttons import *
from indy.commander import *
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

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    # os.system("taskset -p -c 0,1 %d" % os.getpid())

    GLOBAL_FLAG['run'] = True
    GLOBAL_FLAG['test_mode'] = True #test
    from indy.commander import *

    thread_list = []
    th0 = threading.Thread(target=app_ui)
    th0.start()
    thread_list.append(th0)

    th1 = threading.Thread(target=commander)
    th1.start()
    thread_list.append(th1)

    th2 = threading.Thread(target=rt_status_update)
    th2.start()
    thread_list.append(th2)

    th3 = threading.Thread(target=safety_thread)
    th3.start()
    thread_list.append(th3)

    th4 = threading.Thread(target=data_logging)
    th4.start()
    thread_list.append(th4)

    def get_ipaddress():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("10.255.255.255", 1))
            r = s.getsockname()[0]
            s.close()
            return r
        except:
            return "127.0.0.1"

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    ip_addr = get_ipaddress()
    # app.run_server(host=ip_addr, port=8050, debug=False)
    # app.run_server(host=ip_addr, port=8050, debug=True)
