from pyquery import PyQuery
from fake_useragent import UserAgent
import json

ua = UserAgent()

url = "https://www.amz520.com/amztools/amusestimator.html"
headers = {'User-Agent': ua.random}
dom = PyQuery(url, headers=headers)
#获取value
essiteselect = dom("#essiteselect option").text()
ids = [dom(ele).attr("value") for ele in dom("#essiteselect option")]

arr = essiteselect.split()

#获取对应value
def getOptions(countryId):
    obj = {}
    for options in dom("#selectcate%s option" % countryId):
        text = dom(options).text()
        value = dom(options).attr("value")
        obj[text] = value
    return obj


obj = {}
for i in range(0, len(arr)):
    data = {}
    data['id'] = ids[i]
    data['options'] = getOptions(ids[i])
    obj[arr[i]] = data

# 存储格式{"美国":{id:1,options:{'':1}}}

with open('countrys.json', 'w', encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False)

