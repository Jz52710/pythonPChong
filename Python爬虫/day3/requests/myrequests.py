import requests
url = "https://movie.douban.com/top250"
params = {'start':0}
rsp = requests.get(url,params=params,headers={

})
# print(rsp.url) #获取请求地址
# print(rsp.text) #获取详情内容 utf-8
# print(rsp.content) #获取详情内容 字节

# #头条
# url = "https://www.toutiao.com/stream/widget/local_weather/city/"
# res = requests.get(url)
# print(res.json())