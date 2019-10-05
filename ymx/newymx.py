import xlrd,xlwt
from pyquery import PyQuery
from fake_useragent import UserAgent
import requests
import re
import json
import time

#随机生成请求头
ua = UserAgent()

with open('countrys.json', 'r', encoding='utf-8') as f:
    country = json.load(f)

#读取数据
book = xlrd.open_workbook('data.xlsx')
sheet = book.sheet_by_index(0)

def getUrls():
    for row in range(1,sheet.nrows):
        url = sheet.cell_value(row,1)
        status = sheet.cell_value(row,2)
        country = sheet.cell_value(row,3)
        yield url,status,country
# 爬取排名、面包屑、品牌
def getCateRank(url):
    headers = {'User-Agent':ua.random}
    dom = PyQuery(url,headers=headers)
    #面包屑
    categoty = " ".join(dom('#wayfinding-breadcrumbs_feature_div>ul>li:nth-child(1)>span>a').text().split())
    #排名
    if dom('#SalesRank'):
        ranking = re.findall("#([\d,]+?)\s",dom("#SalesRank").text())[0].replace(",","")
    else:
        res = requests.get(url,headers=headers)
        ranking = re.findall("#([\d,]+?)\s[\s\w]+?\(",res.text)[0].replace(",","")
    # 品牌
    if dom('.ac-keyword-link'):
        brand = dom('.ac-keyword-link a').text()
        # print(brand)
    else:
        brand = dom('.badge-wrapper a span span').text()
    return categoty,ranking,brand


#销量
def getSales(rank,category,store):
    try:
        response = requests.get(f'https://api.junglescout.com/api/v1/sales_estimator?rank={rank}&category={category}&store={store}',headers={
            'User-Agent':ua.random,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin':'https://www.junglescout.cn',
            'Referer':'https://www.junglescout.cn/sales-estimator/?gspk=eGlhb2JlaWd1NDkxNA==&gsxid=CbAoPaqzlKhB&utm_medium=xiaobeigu4914&utm_source=affiliate'
        })
        res = response.json()
        return res['estSalesResult']
    except:
        return "数据异常"

# 读取json数据
def getCageIdCounId(coun):
    counid = country[coun]['id']
    cateid = country[coun]['options']
    return cateid,counid
#运行
def save():
    index = 0
    t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    lists = ['id','url','category','Country Abbreviation','country','ranking','brand','sales']
    book = xlwt.Workbook()
    mysheel = book.add_sheet('亚马逊')
    for i in range(0,len(lists)):
        mysheel.write(0,i,lists[i])
    for url,status,countryname in getUrls():
        index+=1
        try:
            categoryname, ranking, brand = getCateRank(url)
            categoryID, countryID = getCageIdCounId(countryname)
            sale = getSales(ranking, categoryID, countryID)
            print(index, categoryname, countryID,countryname,ranking, categoryID,brand,sale)
            mysheel.write(index,0,index)#编号
            mysheel.write(index,1,url)#网址
            mysheel.write(index,2,categoryname)#面包屑
            mysheel.write(index,3,countryID)#1
            mysheel.write(index,4,countryname)  # 美国
            mysheel.write(index,5,ranking)  # 排名
            mysheel.write(index,6,brand)#品牌
            mysheel.write(index,7,sale)#销量
        except BaseException as e:
            print(e)
            # pass
    book.save(t+'.xls')



if __name__ == '__main__':
    save()
    # t = Thread(target=save)
    # t.start()
    # print(urls)