import pybithumb
import pprint
import coinList
import dayAvg
import minute
import balance
import web
import asyncio


f = open("bithumb.txt")
lines = f.readlines()
access = lines[0].strip() #access key
secret = lines[1].strip() #secret key
f.close()

bithumb = pybithumb.Bithumb(access,secret)
coin_list = coinList.get_highest()
volume_rank = []
today_open = []
day_avg= []
min_avg= []
transaction = {}
p=0
balance=balance.get_balance()


for i in range(len(coin_list)):
    coin_list[i] = coin_list[i].split('/')
    volume_rank.append(coin_list[i][0])
print("거래대금 상위 10종목:",volume_rank)

for i in range(len(volume_rank)):
    day_avg.append(dayAvg.get_dayAvg(volume_rank[i]))


for i in range(len(volume_rank)):
    min_avg.append(minute.get_min_avg(volume_rank[i]))


for i in range(len(volume_rank)):
    today_open.append(dayAvg.today(volume_rank[i]))


while True:
    check_price = bithumb.get_orderbook(volume_rank[p])
    asks = check_price['asks'][0]['price'] #매도 1호가
    bids = check_price['bids'][0]['price'] #매수 1호가

    async def main():
        global transaction
        transaction = await web.bithumb_ws_client(volume_rank[p])
    asyncio.run(main())

    print(volume_rank[p], "종목 탐색중...")
    print("5일선:", day_avg[p])
    print("순간체결가:", transaction['contPrice'], "  거래금액:", transaction['contAmt'])

    try:
        if min_avg[p] > day_avg[p] and float(transaction['contAmt']) > 1000000.0 and float(transaction['contPrice']) >= day_avg[p]:
            order = bithumb.buy_limit_order(volume_rank[p], asks, (balance // asks) * 0.8)
            print("매수체결")
            print(order)
            break

    except Exception as e:
        print(e)

    p=p+1
    if(p==10):
        p=0

