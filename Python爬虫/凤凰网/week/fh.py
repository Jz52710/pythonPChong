from pyquery import PyQuery


# 初始化方式
# PyQuery(url="https://www.baidu.com")
# PyQuery("<html><div></div></html>")
# PyQuery(filename="index.html")

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def updata(urls):
    ifeng = PyQuery(url=urls,headers=headers)
    #标题
    title = ifeng(".news-stream-newsStream-mr13 a")
    #内容
    con = ifeng('.news-stream-newsStream-mr13 a')
    content = con.attr("href")
    #来源
    source = ifeng('.clearfix .news-stream-newsStream-mr10')
    #时间
    times = ifeng('.clearfix time')
    # print(box.attr("class"))
    print(title.text())
    print(source.text())
    print(times.text())
    print(content)

updata("http://news.ifeng.com/")