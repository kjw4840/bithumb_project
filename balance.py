import fileOpen

bithumb = fileOpen.file_opne()
def get_balance():
    balance = bithumb.get_balance("BTC")
    return balance[2]



