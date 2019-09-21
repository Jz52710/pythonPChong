import requests
import time
import json
import urllib3
import sys
import hashlib
from threading import Thread

urls = ["https://fe-api.zhaopin.com/c/i/sou?pageSize=%s&cityId=576"%i for i in range(0,10)]
'''
city = ['576','577','578','579','580']
urls = ["https://fe-api.zhaopin.com/c/i/sou?pageSize=10&cityId=%s"%i for i in city]
print(urls)
'''
class Recruit(Thread):
    def __init__(self):
        super(Recruit,self).__init__()
    def run(self):
        item = {}
        while len(urls)>0:
            url = urls.pop()
            '''
            代理
            '''
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            _version = sys.version_info

            is_python3 = (_version[0] == 3)

            orderno = "ZF20199183769jXKFig"
            secret = "dadeedefdbdd4c7da573790de267d0a2"

            ip = "forward.xdaili.cn"
            port = "80"

            ip_port = ip + ":" + port

            timestamp = str(int(time.time()))
            string = ""
            string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

            if is_python3:
                string = string.encode()

            md5_string = hashlib.md5(string).hexdigest()
            sign = md5_string.upper()
            # print(sign)
            auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

            # print(auth)
            proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
            headers = {"Proxy-Authorization": auth,
                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
                       }

            res = requests.get(url, headers=headers, proxies=proxy, verify=False,allow_redirects=False).text
            data = json.loads(res)['data']['results']
            for i in range(0, len(data)):
                item['title'] = data[i]['jobName']
                item['pay'] = data[i]['salary']
                item['site'] = data[i]['city']['display']
                item['degree'] = data[i]['eduLevel']['name']
                item['company'] = data[i]['company']['name']
            print(self.name,item)
            with open('job.json', 'a+', encoding="utf-8") as f:
                json.dump(item, f, ensure_ascii=False)


for i in range(3):
    mytest = Recruit()
    mytest.start()
'''
print(len(urls))
print(urls)
'''