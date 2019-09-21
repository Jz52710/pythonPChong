from urllib.request import urlopen
import lxml.etree as et

for m in range(1,3):
    url = f"http://soso.huitu.com/search?kw=%E4%B8%AD%E7%A7%8B&page={m}"


rep = urlopen(url)
#类似于上下文管理器
res = rep.read().decode()

htmlobj = et.HTML(res)
html = htmlobj.xpath("//div[@class = 'seozone']/a/img/@originalsrc")
# print(html)
#下载
def upload(url):
    filename = "汇图网中秋图片/"+url.split("/")[-1]
    print('下载'+url.split("/")[-1])
    with open(filename,'wb') as f:
        f.write(urlopen(url).read())
for i in html:
    upload(i)