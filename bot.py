#텔레그램 봇 체결알림
import telegram

# token
def buy_sendMessage(text):
    with open("./token.txt") as f:
        lines = f.readlines()
        token = lines[0].strip()

    # bot
    bot = telegram.Bot(token = token)

    bot.sendMessage(chat_id=1419888091,text="매수가 체결 되었습니다.\n"+str(text[0][1])+"/체결가:"+str(text[1])+"/수량:"+str(text[2]))

def sell_sendMessage(text):
    with open("./token.txt") as f:
        lines = f.readlines()
        token = lines[0].strip()

    # bot
    bot = telegram.Bot(token = token)

    bot.sendMessage(chat_id=1419888091,text="매도가 체결 되었습니다.\n"+str(text[1])+"/체결가:"+str(text[2])+"/수량:"+str(text[3]))



