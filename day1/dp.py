from urllib.request import urlopen
from urllib import error
import lxml.etree as etree
import time
import xlwt

class DBSpider:
    def __init__(self):
        self.urls = [ 'https://movie.douban.com/top250?start=%s'%i for i in range(0,250,25)]
        self.time = 5
        self.book = xlwt.Workbook()
        self.sheet = self.book.add_sheet("豆瓣电影Top250")
    def getPage(self,url):
        try:
            # 数据挖掘
            pageData = urlopen(url).read().decode()
        except error.URLError as e:
            print(e)
        else:
            return pageData

    def pageParse(self,data):
        # 数据解析
        htmlObj = etree.HTML(data)
        # 电影名
        title = htmlObj.xpath("//div[@class='item']/div[@class='info']//span[@class='title'][1]/text()")
        # 导演
        dire = htmlObj.xpath("//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()")
        dire = [ i.strip() for i in dire]
        dire = [ dire[i]+dire[i+1] for i in range(0,50,2)]
        # 评分
        score = htmlObj.xpath("//div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[2]/text()")
        # 简介
        info = htmlObj.xpath("//div[@class='item']/div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()")

        return list(zip(title,dire,score,info))

    def save(self,data):
        for i in range(len(data)):
            # 电影名
            self.sheet.write(i,0,data[i][0])
            # 导演
            self.sheet.write(i, 1, data[i][1])
            # 评分
            self.sheet.write(i, 2, data[i][2])
            # 简介
            self.sheet.write(i, 3, data[i][3])
        self.book.save("豆瓣电影top250.xls")

    def run(self):
        arr = []
        for url in self.urls:
            print("%s正在下载.."%url)
            time.sleep(self.time)
            data = self.getPage(url)
            t = self.pageParse(data)
            arr+=t
        self.save(arr)


db = DBSpider()
db.run()

