# 이동평균선

import pybithumb

def get_dayAvg(ticker):
    close = 0
    cnt = 0
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-5:]
    for i in range(len(yesterday)):
        close += yesterday['close'][i]
        cnt+=1
    close = close / cnt
    return close

def today(ticker):
    df = pybithumb.get_ohlcv(ticker)
    today = df.iloc[-1]
    today_open = today['open']
    return today_open

