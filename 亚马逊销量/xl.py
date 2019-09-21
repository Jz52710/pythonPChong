from pyquery import PyQuery
import xlwt

class updata:
    def __init__(self):
        self.value = []
        self.font = ''
        self.url ='https://www.amz520.com/amztools/amusestimator.html'
        self.headers = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    def sales(self):
        sales = PyQuery(url=self.url,headers=self.headers)
        # print(sales)
        # 面包屑值
        fonts = sales('.pull-right select').text()
        fonta = fonts[24:].strip().split("\n")
        self.font = fonta
        # print(fonta)
        # print(fonts)
        print(self.font)
        print(len(self.font))
        # value值
        valuu = sales('.input-group select option').items()
        print(valuu)
        for i in valuu:
            val = i.attr('value')
            self.value.append(val)
            # print(val)
        # print(valuu)
        for j in range(0,7):
            del self.value[0]
        print(self.value)
        print(len(self.value))




g = updata()
g.sales()