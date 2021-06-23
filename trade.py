# 매수,매도
import asyncio
import web
import fileOpen

buy_transaction = []
sell_transaction = []


# 매수
def buy_Ticker(ticker, five_day, min_avg, balance):
    p = 0
    bithumb = fileOpen.file_opne()
    while True:
        check_price = bithumb.get_orderbook(ticker[p])
        asks = check_price['asks'][0]['price']  # 매도 1호가
        check_zero = str(asks).split('.')
        buy_order = []
        uint = 0
        if int(check_zero[1]) == 0:
            asks = int(asks)
        try:
            async def main():
                global buy_transaction
                buy_transaction = await web.bithumb_ws_client_bid(ticker[p])

            asyncio.run(main())

            print(ticker[p], "종목 탐색중...")
            print("5일선:", five_day[p])
            print("순간체결가:", buy_transaction['contPrice'], "  거래금액:", buy_transaction['contAmt'])
            if asks > balance:
                unit = round((balance / asks) * 0.8, 5)
            else:
                unit = balance // asks * 0.8
            if min_avg[p] > five_day[p] and float(buy_transaction['contAmt']) > 1000000.0 and float(
                    buy_transaction['contPrice']) >= five_day[p]:
                order = bithumb.buy_limit_order(ticker[p], asks, unit)
                print(ticker[p], asks, balance)
                print("매수체결", order)
                buy_order.append(order)
                buy_order.append(asks)
                buy_order.append(unit)
                return buy_order

        except Exception as e:
            print(e)
            continue

        p = p + 1
        if (p == len(ticker)):
            p = 0


# 매도
def sell_Ticker(ticker, asks):
    up = asks * 0.03
    down = asks * 0.05
    sell_order = []
    bithumb = fileOpen.file_opne()
    unit = bithumb.get_balance(ticker)[0]
    while True:
        check_price = bithumb.get_orderbook(ticker)
        bids = check_price['bids'][0]['price']  # 매수 1호가
        check_zero = str(bids).split('.')
        if int(check_zero[1]) == 0:
            bids = int(bids)

        try:
            async def main():
                global sell_transaction
                sell_transaction = await web.bithumb_ws_client(ticker)

            asyncio.run(main())
            print("매도 대기중..")
            print("순간체결가:", sell_transaction['contPrice'], "  거래금액:", sell_transaction['contAmt'])

            if float(sell_transaction['contPrice']) > asks + up:
                order = bithumb.sell_limit_order(ticker, bids, unit)
                print("매도체결", order)
                sell_order.append(order)
                sell_order.append(ticker)
                sell_order.append(bids)
                sell_order.append(unit)
                return sell_order

            elif float(sell_transaction['contPrice']) < asks - down:
                order = bithumb.sell_limit_order(ticker, bids, unit)
                print("매도체결", order)
                sell_order.append(order)
                sell_order.append(ticker)
                sell_order.append(bids)
                sell_order.append(unit)

                return sell_order
        except Exception as e:
            print(e)
            continue
