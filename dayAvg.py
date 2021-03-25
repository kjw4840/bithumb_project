# 이동평균선

import pybithumb

def get_dayAvg(ticker):
    close = 0
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-5:]
    for i in range(5):
        close += yesterday['close'][i]
    close = close / 5
    return close

def today(ticker):
    df = pybithumb.get_ohlcv(ticker)
    today = df.iloc[-1]
    today_open = today['open']
    return today_open

