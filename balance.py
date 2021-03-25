import pybithumb


f = open("bithumb.txt")
lines = f.readlines()
access = lines[0].strip() #access key
secret = lines[1].strip() #secret key
f.close()


bithumb = pybithumb.Bithumb(access,secret)

def get_balance():
    balance = bithumb.get_balance("BTC")
    return balance[2]
