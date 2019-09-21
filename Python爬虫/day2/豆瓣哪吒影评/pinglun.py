from urllib.request import urlopen
import lxml.etree as et
import pickle

data = []
for ig in range(0,10):
    url = f'https://movie.douban.com/subject/26794435/comments?start={20*ig}&limit=20&sort=new_score&status=P&percent_type=h'
    con = urlopen(url).read().decode()
    htmlObj = et.HTML(con)
    yp = htmlObj.xpath('//span[@class="short"]/text()')
    print('正在下载%s'%url)
    for i in yp:
        data.append(i)
with open('哪吒影评.txt','wb') as f:
    pickle.dump(data,f)
