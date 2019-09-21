import requests
import lxml.etree as et
import json
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pickle

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data = {}

# def  updata(urls):
#     res = requests.get(url=urls,headers=headers)
#     re = res.text
#     ress = et.HTML(re)
#     title = ress.xpath('//h2/a/text()')
#     print(title)
#
# url = 'http://tech.ifeng.com/'
# updata(url)
class updata():
    def __init__(self):
        urls = 'http://tech.ifeng.com/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        data = {}
        self.url = urls
        self.headers = headers
    def pa(self):
        res = requests.get(url=self.url,headers=self.headers)
        re = res.text
        ress = et.HTML(re)
        #标题
        title = ress.xpath('//h2/a/text()')
        #链接
        content = ress.xpath('//h2/a/@href')
        for i in content:
            href = "http:"+i
            nr = requests.get(url=href,headers=self.headers)
            nrr = nr.text
            nro = et.HTML(nrr)
            nr = nro.xpath('//script[5]/text()')
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
            rong2 = rong1.split('[{"data":')
            rong3 = rong2[1]
            rong4 = rong3.split('"type"')
            rong5 = rong4[0]

            # print(rong4[0])
            # print(len(rong4))
            # print(rong2)
            # print(len(rong2))
            # new = re.search('<p>[]</p>',rong5)
            # print(new)
            # pat = re.compile("<p>r'[\u4e00-\u9fa5]+'<\p>")
            # result = pat.findall(rong5)
            result = re.math(r".*?([\u4E00-\u9FA5])",rong5)
            print(result)
            # print(href)
        # print(content)
        #来源
        source = ress.xpath('//div[@class="clearfix"]/span/text()')
        #时间
        times = ress.xpath('//div[@class="clearfix"]/time/text()')
        # print(source)
        # print(times)
        # data['title'] = title
        # print(data)
a = updata()
a.pa()
#保存
# with open("财经.py","wb") as f:
#     pickle.dump(data,f)
# print(data)
