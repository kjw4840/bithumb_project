#체결/미체결 확인 timer
import threading
import fileOpen

bithumb = fileOpen.file_opne()
s = 0
tic = ""

def timer(*ticker):
    global tic
    global s
    tic = ticker
    balance = bithumb.get_balance(str(tic).split('\'')[1])
    if balance[3] == 0:
        return True
    s += 1
    if s == 10:
        return False
    threading.Timer(10, timer,args=ticker,kwargs=None).start()


