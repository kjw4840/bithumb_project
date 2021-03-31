import coinList
import dayAvg
import minute
import balance
import trade
import fileOpen
import timer
import time
import bot

bithumb = fileOpen.file_opne()
coin_list = coinList.get_highest()
volume_rank = []
today_open = []
day_avg = []
min_avg = []
transaction = {}
p = 0
balance = balance.get_balance()

for i in range(len(coin_list)):
    coin_list[i] = coin_list[i].split('/')
    volume_rank.append(coin_list[i][0])
print("거래대금 상위 종목:", volume_rank)

for i in range(len(volume_rank)):
    day_avg.append(dayAvg.get_dayAvg(volume_rank[i]))

for i in range(len(volume_rank)):
    min_avg.append(minute.get_min_avg(volume_rank[i]))

for i in range(len(volume_rank)):
    today_open.append(dayAvg.today(volume_rank[i]))

while True:
    #매수
    buy_order = trade.buy_Ticker(volume_rank, day_avg, min_avg, balance)
    time.sleep(5)


    # 미체결/체결 확인
    timers = timer.timer(buy_order[0][1])

    if not timers:
        cancel = bithumb.cancel_order(buy_order[0])
        print("미체결 주문 취소", cancel)
        continue
    bot.buy_sendMessage(buy_order)

    # 매도
    sell_order = trade.sell_Ticker(buy_order[0][1], buy_order[1])

    # 미체결/체결 확인
    timers = timer.timer(sell_order[0][1])

    bot.sell_sendMessage(sell_order)




