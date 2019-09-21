import requests,json
import time
from fake_useragent import UserAgent
ua = UserAgent()
import re

class IfengSpider:
    def __init__(self):
        self.urls = [
            'https://shankapi.ifeng.com/autumn/xijinping/index/getCustomNewsTfList/0/%s/getCustomData?callback=getCustomData&_=120',
            'https://shankapi.ifeng.com/shanklist/_/getColumnInfo/_/default/6579208763817865234/1568606247000/%s/3-35199-/getColumnInfoCallback?callback=getColumnInfoCallback&_=15686334114231',  # 台湾
            'https://shankapi.ifeng.com/shanklist/_/getColumnInfo/_/default/6572044442780307492/1566891029000/%s/3-35190-/getColumnInfoCallback?callback=getColumnInfoCallback&_=15686334318081', # 暖新闻
            'https://shankapi.ifeng.com/autumn/xuanzhan/index/getCustomNewsTfList/0/%s/getCustomData?callback=getCustomData&_=120' # 宣战2020
        ]
        self.data = {
            #'':{'con':"",'edit':'','date':"",'source':''}
        }
    #新时代
    def newSpiderList(self,num):
        """
        新时代新气象 列表页
        :param num:
        :return:
        """
        # url = 'https://shankapi.ifeng.com/autumn/xijinping/index/getCustomNewsTfList/0/%s/getCustomData?callback=getCustomData&_=120'%num
        url = self.urls[0]%num
        resp = requests.get(url,headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent':ua.random
        })
        res = json.loads(resp.text[14:-1])
        data = res['data']['newsstream']
        for obj in data:
           yield obj['url']

    def newSpiderCon(self):
        urls = self.newSpiderList(10)
        for url in urls:
            resp = requests.get(url,headers={
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'User-Agent':ua.random
            })
            data = re.findall("var allData = (.+?});",resp.text)
            data = json.loads(data[0])["docData"]
            title = data['title']
            source = data['source']
            date = data['newsTime']
            try:
                edit = data['editorName']
            except:
                edit = "空"
            con = data['contentData']
            self.save(title=title,date=date,source=source,con=con,edit=edit)
            print("《%s》下载完成..."%title)
            time.sleep(3)
    #台湾
    def taiWanList(self,num1):
        url = self.urls[1]%num1
        resp = requests.get(url, headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': ua.random
        })
        res = json.loads(resp.text[22:-1])
        # print(res)
        data = res['data']['newsstream']
        for obj in data:
            yield obj['url']
    def taiWanCon(self):
        urls = self.taiWanList(10)
        for url in urls:

            resp = requests.get(url, headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'User-Agent': ua.random
            })
            data = re.findall("var allData = (.+?});", resp.text)
            data = json.loads(data[0])["docData"]
            title = data['title']
            source = data['source']
            date = data['newsTime']
            try:
                edit = data['editorName']
            except:
                edit = "空"
            con = data['contentData']
            self.save(title=title, date=date, source=source, con=con, edit=edit)
            print("《%s》下载完成..." % title)
            time.sleep(3)
    # 暖新闻
    def nuanNewsList(self,num2):
        url = self.urls[2]%num2
        resp = requests.get(url, headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': ua.random
        })
        res = json.loads(resp.text[22:-1])
        # print(res)
        data = res['data']['newsstream']
        for obj in data:
            yield obj['url']
    def nuanNewCon(self):
        urls = self.nuanNewsList(10)
        for url in urls:
            resp = requests.get(url, headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'User-Agent': ua.random
            })
            data = re.findall("var allData = (.+?});", resp.text)
            data = json.loads(data[0])["docData"]
            title = data['title']
            source = data['source']
            date = data['newsTime']
            try:
                edit = data['editorName']
            except:
                edit = "空"
            con = data['contentData']
            self.save(title=title, date=date, source=source, con=con, edit=edit)
            print("《%s》下载完成..." % title)
            time.sleep(3)
    # 2020
    def xuanZanList(self,num3):
        url = self.urls[3]%num3
        resp = requests.get(url, headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': ua.random
        })
        res = json.loads(resp.text[14:-1])
        # print(res)
        data = res['data']['newsstream']
        for obj in data:
            yield obj['url']
    def xuanZanCon(self):
        urls = self.xuanZanList(10)
        for url in urls:
            resp = requests.get(url, headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'User-Agent': ua.random
            })
            data = re.findall("var allData = (.+?});", resp.text)
            data = json.loads(data[0])["docData"]
            title = data['title']
            source = data['source']
            date = data['newsTime']
            try:
                edit = data['editorName']
            except:
                edit = "空"
            con = data['contentData']
            self.save(title=title, date=date, source=source, con=con, edit=edit)
            print("《%s》下载完成..." % title)
            time.sleep(3)
    # 保存
    def save(self,title,con,edit,date,source):
        if title not in self.data:
            self.data[title]={'con':con,'edit':edit,'date':date,'source':source}
        with open('凤凰.txt','w',encoding="utf-8") as f:
            json.dump(self.data,f,ensure_ascii=False)



s = IfengSpider()
s.newSpiderCon()
s.taiWanCon()
s.nuanNewCon()
s.xuanZanCon()
# print(s.data)
