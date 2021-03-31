# 5분봉
import pybithumb
import requests
import pandas as pd

def get_min_avg(ticker):
    data = requests.get('https://api.bithumb.com/public/candlestick/'+ticker+'_KRW/3m')
    data = data.json()
    data = data.get("data")
    df = pd.DataFrame(data)
    df = df.tail(3)[2]
    min_avg = 0.0
    for item in df:
        min_avg = min_avg + float(item)
    min_avg = min_avg / 3
    return min_avg

