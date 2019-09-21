from urllib.request import urlopen,Request
import lxml.etree as et

url =r'C:\Users\MI\Desktop\Python爬虫\day3\Xpath\dd.html'
con = urlopen(url).read().decode()
htmlObj = et.HTML(con)
yp = htmlObj.xpath('//div[@class = "box"]')
print(con)