# import win32api
# import win32con

# def handler_func(dwCtrlType):
#     if dwCtrlType == win32con.CTRL_LOGOFF_EVENT or dwCtrlType == win32con.CTRL_SHUTDOWN_EVENT:
#         result = input("Are you sure you want to shut down? (y/n)")
#         if result.lower() == "n":
#             return True
#     return False

# win32api.SetConsoleCtrlHandler(handler_func, True)

import signal

# Catch SIGTERM signal
def handler(signum, frame):
    print("Shutdown prevented")

signal.signal(signal.SIGTERM, handler)

# Your Python code here