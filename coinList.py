#빗썸 거래대금 상위 10종목 출력
import time
from selenium import webdriver

def get_highest():
    browser=webdriver.Chrome('./chromedriver')
    browser.get('https://www.bithumb.com/')
    time.sleep(3)
    coin_list = []
    for i in range(4,14) :
        coin_list.append(browser.find_element_by_xpath('//*[@id="sise_list"]/tbody/tr['+str(i)+']/td[1]/div/p/a/span').text)
    coin_list=' '.join(coin_list).split()
    return coin_list








