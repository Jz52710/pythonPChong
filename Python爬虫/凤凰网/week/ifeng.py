import requests
import lxml.etree as et
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pickle



headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data = {}
def updata(urls):
    res = requests.get(urls,headers=headers)
    re = res.text
    ress = et.HTML(re)
    #标题
    title = ress.xpath('//h2/a/text()')
    #内容
    # contenta = ress.xpath('//h2/a/@href')
    # for i in contenta:
    #     # print(i)
    #     # driverxq = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    #     driver.get("http:"+i)
    #     xq = ActionChains(driver)
    #     dian = driver.find_element_by_class_name("news-stream-newsStream-image-link")
    #     xq.click(dian).perform()
    #     time.sleep(3)
    #     xqy = requests.get("http:"+i,headers=headers)
    #     xqw = xqy.text
    #     xiangq = et.HTML(xqw)
    #     xp = xiangq.xpath('//div[@id="text-3zQ3cZD4"]')
    #     print(xp)
    #     driver.back()
    #     # driver.forward()  # 前进
    #     # driver.back()  # 后退
    content = ress.xpath('//h2/a/@href')
    # content = ['http:'+contents]
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


updata("http://news.ifeng.com/")

print(data)