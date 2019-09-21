import requests
import lxml.etree as et
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pickle

#伪装头
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data = {}
sub = []
#打开凤凰
def updata(urls):
    res = requests.get(url=urls,headers=headers)
    re = res.text
    ress = et.HTML(re)
    # print(ress)
    #标题
    title = ress.xpath('//h2/a/text()')
    #内容
    contenta = ress.xpath('//h2/a/@href')
    for i in contenta:
        driverxq = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driverxq.get("http:"+i)
        xq = ActionChains(driverxq)
        dian = driverxq.find_element_by_class_name("text-3zQ3cZD4")
        nei = dian.text
        sub.append(nei)
        print("正在爬取%s"%i)
        time.sleep(3)
        driverxq.close()
    # content = ress.xpath('//h2/a/@href')
    # 来源
    source = ress.xpath('//div[@class="clearfix"]/span/text()')
    # #时间
    times = ress.xpath('//div[@class="clearfix"]/time/text()')
    #添加到data
    data['title'] = title
    data['content'] = sub
    data['source'] = source
    data['times'] = times

#输入凤凰网
# url1 = "http://news.ifeng.com/"
url1 = "http://tech.ifeng.com/"
updata(url1)
#二进制保存
# with open('凤凰.txt', 'wb') as f:
#     pickle.dump(data, f)
with open('科技.txt', 'wb') as f:
    pickle.dump(data, f)
print(data)
# print(sub)