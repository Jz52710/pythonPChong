import xlwt
from pyquery import PyQuery
import time
import requests
import re

class upData:
    def __init__(self):
        self.mb =[]
        self.top = []
        self.urls=[]
        self.headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    def pyymx(self):
        with open('链接.txt','r') as f:
            a= f.readlines()
        for i in a:
            b = "".join(i).strip()
            # self.lj.append(b)
            self.urls.append(b)
        print(self.urls)
        #打开链接
        for u in self.urls:
            time.sleep(3)
            ymx = PyQuery(url=u,headers=self.headers)
            # time.sleep(3)
            # print(ymx)
            #面包屑
            mbx = ymx('#wayfinding-breadcrumbs_feature_div ul li span a').text()
            self.mb.append(mbx)
            # print(mbx)
            #排名
            top = ymx('#SalesRank .value').remove('style').text()
            a = top.replace(' ','').split()
            b = ' '.join(a)
            self.top.append(b)
            # print(top)
            # print(b)
            # c = re.findall("#([\d,]+?)\s[\s|\w]+?\(",ymx('#SalesRank').text())[0]

            # print(c)
    def save(self):
        book = xlwt.Workbook()
        mydata = book.add_sheet('亚马逊')
        for i in range(0,len(self.urls)):
            try:
                mydata.write(i,0,self.urls[i])
                mydata.write(i,1,self.mb[i])
                mydata.write(i,2,self.top[i])
            except:
                mydata.write('空')
        book.save('ymx.xls')

g = upData()
g.pyymx()
g.save()