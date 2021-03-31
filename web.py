import websockets
import json

#매수 실시간 체결
async def bithumb_ws_client_bid(ticker):
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:

        subscribe_fmt = {
            "type":"transaction",
            "symbols": [ticker+"_KRW"],
            "tickTypes": ["MID"]
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            if list(data.keys())[1] == 'content' and data['content']['list'][0]['buySellGb'] == "2":
                transaction = data['content']['list'][0]
                return transaction

#매도,매수  실시간 체결
async def bithumb_ws_client(ticker):
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:

        subscribe_fmt = {
            "type":"transaction",
            "symbols": [ticker+"_KRW"],
            "tickTypes": ["MID"]
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            if list(data.keys())[1] == 'content':
                transaction = data['content']['list'][0]
                return transaction

