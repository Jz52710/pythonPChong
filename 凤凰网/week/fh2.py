import requests
import lxml.etree as et
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pickle
import json



headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data = {}

# driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver.get("http://news.ifeng.com/")
# time.sleep(3)
# # 创建事件对象
# action = ActionChains(driver)
# geng = driver.find_element_by_class_name('news-stream-basic-more')
# action.click(geng).perform()
# time.sleep(3)

res = requests.get("http://news.ifeng.com/",headers=headers)
re = res.text
ress = et.HTML(re)
# print(ress)
#标题
title = ress.xpath('//h2/a/text()')
#内容
contenta = ress.xpath('//h2/a/@href')
for i in contenta:
    # print(i)
    # driverxq = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    # driverxq.get("http:"+i)
    # xq = ActionChains(driverxq)
    # dian = driverxq.find_element_by_class_name("news-stream-newsStream-image-link")
    # xq.click(dian).perform()
    xq = requests.get("http:"+i)
    xiang = xq.text
    xiangq = et.HTML(xiang)
    # fh = json.loads(xiang.strip('var allData = '))
    # print(fh)
    nr = xiangq.xpath('//script[5]/text()')
    a = "".join(nr).strip()
    b = a.split('\n')
    # print(b)
    # print(len(b))
    nei = b[0].strip('var allData = ')
    # print(nei)
    rong = nei.split('"contentList":')
    rong1 = rong[1]
    # print(rong1)
    # print(len(rong1))
    rong2 = rong1.split(',')
    rong3 = rong2[0]
    rong4 = rong3.strip('[{"data":"')
    # print(rong2[0])
    # print(len(rong2))
    rong5 = rong4.split('<p>')
    print(rong5)
    # print(len(rong5))
    # print(rong4)
    # print(rong[1])
    # print(len(rong))
    # print(type(rong))
    # print(type(nei))
    # print(len(b))
    # print(nr)
    # print(a)
    # print(b)
    # fh = json.loads(a.strip('var allData = '))
    # print(fh["noffhFlag"])
    # print(fh)
    # print(xiang)
    time.sleep(3)
content = ress.xpath('//h2/a/@href')
# #来源
source = ress.xpath('//div[@class="clearfix"]/span/text()')
# #时间
times = ress.xpath('//div[@class="clearfix"]/time/text()')

data['title'] = title
data['content'] = content
data['source'] = source
data['times'] = times

    # with open('咨询.txt', 'wb') as f:
    #     pickle.dump(data, f)




# print(data)