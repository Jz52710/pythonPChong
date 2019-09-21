from urllib.request import urlopen,Request
from urllib.parse import parse_qs
import lxml.etree as et
import time
from sys import argv

# def login(*args):
#     input(f'请输入歌手{args}')

url = Request(f'https://music.163.com/artist?id={argv[1]}',headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'referer':'https://music.163.com/'
})

con = urlopen(url).read().decode()
# print(type(con))
htmlObj = et.HTML(con)

yy =htmlObj.xpath('//ul[@class="f-hide"]/li/a/@href')
filenames = htmlObj.xpath('///ul[@class="f-hide"]/li/a/text()')
ids = [i[9:] for i in yy]
data = zip(filenames,ids)

def updata(filenam,id):

    req = Request("https://music.163.com/song/media/outer/url?id=%s"%id,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'referer':'https://music.163.com/'
    })
    datas =urlopen(req).read()
    with open('song/%s.mp3'%filenam,'wb') as f:
        f.write(datas)
    print('%s下载中...'%filenam)
    # time.sleep(3)
for filename,id in data:
    updata(filename,id)

