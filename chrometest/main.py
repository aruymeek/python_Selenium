from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


##### Chromedriver를 이용하여 crawling 하기 #####
from model.stock import StockModel

driver = webdriver.Chrome()
url = 'https://finance.naver.com/world'
driver.get(url)


##### html 소스 가져오기 #####
table = driver.find_element_by_xpath('//*[@id="americaIndex"]')
# '//tr' 앞에 '.'이 붙은 이유는 table의 하위에서 tr을 찾으라는 의미!
# 그냥 '//tr'만 쓰면 전체 코드에서 tr이 들어간 부분들을 모두 찾아냄
trs = table.find_elements_by_xpath('.//tr')


##### 데이터 crawling 후 model로 인스턴스 만들기 #####
stockList = []

for tr in trs:
    tds = tr.find_elements_by_xpath('.//td')

    if len(tds) == 0:
        continue
    else:
        nation = tds[0].text
        index = tds[1].text
        now = float(tds[2].text.replace(',', ''))
        diff = float(tds[3].text.replace(',', ''))
        percent = float(tds[4].text.replace('%', ''))
        
        #그래프(너비)는 어떻게 가져올까?
        span = tds[5].find_element_by_xpath('.//span')
        #.get_attribute('속성'): 해당 속성의 값을 반환함
        style = span.get_attribute('style')
        graph_width = float(style.split(': ')[1].replace('%', '').replace(';', ''))

        #time = tds[6].text

        stock = StockModel(nation, index, now, diff, percent)
        stockList.append(stock)


##### txt 파일로 저장하기 #####
f = open(r'C:\Users\671\Desktop\y\python\chrometest\stock.txt', 'w', encoding="utf-8")

for stock in stockList:
    line = stock.SaveFormat()

    f.write(line)
    f.write('\n')

f. close()


