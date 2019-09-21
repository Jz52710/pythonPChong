from urllib.request import urlopen
import lxml.etree as et
import xlwt

daoy = []
zhuy = []
zi1 = []
pf1 = []
jj1 = []
for ig in range(0,10):
    url = f"https://movie.douban.com/top250?start={25*ig}"
    html = urlopen(url).read().decode()
    htmlObj = et.HTML(html)

    zi = htmlObj.xpath("//div[@class = 'hd']/a/span[1]/text()")
    dy = htmlObj.xpath("//div[@class = 'bd']/p[1]/text()")
    pf = htmlObj.xpath("//div[@class = 'star']/span[@class = 'rating_num']/text()")
    jj = htmlObj.xpath("//p[@class = 'quote']/span/text()")
    dy1 = []
    print('正在下载%s'%url)
    #名字
    for a in zi:
        z =''.join(a).strip()
        # z1 = z.split()
        zi1.append(z)
    #导演
    for a in dy:
        b = ''.join(a).strip()
        # d = b.split('\n')#时间和导演分开
        c = b.split('\xa0\xa0\xa0')#导演主演分开
        dy1.append(c)
    for i in range(0,len(dy1),2):
        dao = dy1[i][0]
        daoy.append(dao)
    #主演
    for q in range(0,len(dy1),2):
        try:
            zhu = dy1[q][1]
        except:
            zhu = '无'
        zhuy.append(zhu)
    #评分
    for a in pf:
        pf1.append(a)
    #简介
    for j in jj:
        jj1.append(j)

# 读
book = xlwt.Workbook()
mysheel = book.add_sheet('豆瓣')
#电影名
for i in range(0,len(zi1)):
    mysheel.write(i,0,zi1[i])
#导演
    mysheel.write(i,1,daoy[i])
#主演
    mysheel.write(i,2,zhuy[i])
#评分
    mysheel.write(i,3,pf1[i])
#简介
    try:
        mysheel.write(i,4,jj1[i])
    except:
        mysheel.write(i,4,"无")

book.save('豆瓣.xls')
