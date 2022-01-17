import signal, os
from examples import sample_main as sm

hProcess = sm.ProcessHandler()

def sig_handler(signum, frame):
    print('SIGNAL RECEIVED:', signum)
    hProcess.terminate()

if __name__ == "__main__":
    os.system("taskset -p -c 0,1 %d" % os.getpid())

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)
    
    hProcess.run()
