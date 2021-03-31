import pybithumb
def file_opne():
    f = open("bithumb.txt")
    lines = f.readlines()
    access = lines[0].strip() #access key
    secret = lines[1].strip() #secret key
    f.close()
    return pybithumb.Bithumb(access,secret)
