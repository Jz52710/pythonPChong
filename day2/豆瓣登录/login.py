from urllib.request import urlopen,Request,HTTPHandler,ProxyHandler,build_opener,HTTPCookieProcessor
import http.cookiejar
import lxml.etree as et
import pickle
from urllib.parse import parse_qs
import json

nzyp =[]
url='https://accounts.douban.com/j/mobile/login/basic'
data = {
    'name':'18634688517',
    'password':'jz52710',
    'remember':'false'
}

req = Request(url,headers={
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
},data=b'ck=&name=18634688517&password=jz52710&remember=false&ticket=')

# 创建cookiejar对象
cookie =http.cookiejar.CookieJar()
hander =HTTPCookieProcessor(cookie)
opener = build_opener(hander)
con =opener.open(req).read()

for i in range(0,20):
    req2 = Request(f"https://movie.douban.com/subject/26794435/comments?start={20*i}&limit=20&sort=new_score&status=P",
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                 })
    res = opener.open(req2)
    res1 = res.read().decode()
    # print(res.read().decode())
    htmlObj = et.HTML(res1)
    yp = htmlObj.xpath('//span[@class = "short"]/text()')
    print("正在下载%s"%req2)
    # print(yp)
    for i in yp:
        nzyp.append(i)
with open('哪吒.txt','wb') as f:
    pickle.dump(nzyp,f)