from pyquery import PyQuery
from fake_useragent import UserAgent
import json

ua = UserAgent()
urls = "https://www.junglescout.cn/sales-estimator/?gspk=eGlhb2JlaWd1NDkxNA==&gsxid=CbAoPaqzlKhB&utm_medium=xiaobeigu4914&utm_source=affiliate"

headers = {'User-Agent': ua.random}
dem = PyQuery(urls, headers=headers)
#获取国家
arr = [dem(i).text() for i in dem('.js-est-stores-list li span')]
# print(arr)
#国家前面的id
ids = [dem(i).attr("data-store") for i in dem('.js-est-stores-list li')]
# print(ids)

#美国input
def us():
    # 美国：{"id:1,optios:{内容}}
    category1 = [dem(i).attr('data-category') for i in dem('.js-est-categories-list .us-available')]
    value1 = [dem(i).text() for i in dem('.js-est-categories-list .us-available span')]
    us1 = dict(zip(value1,category1))
    # print(us1)
    return us1
us()

#英国input
def uk():
    # uk
    value2 = [dem(i).text() for i in dem('.js-est-categories-list .uk-available span')]
    category2 = [dem(i).attr('data-category') for i in dem('.js-est-categories-list .uk-available')]
    uk1 = dict(zip(value2,category2))
    # print(uk1)
uk()

#sapin input
def es():
    # #spain..20
    value3 = [dem(i).attr('data-es-category') for i in dem('.js-est-categories-list .es-available')]
    value31 = [dem(j).text() for j in dem('.js-est-categories-list .es-available span')][19]
    value3.append(value31)
    v3 = list(filter(None,value3))
    category3 = [dem(i).attr('data-category') for i in dem('.js-est-categories-list .es-available')]
    es1 = dict(zip(v3,category3))
    # print(es1)
es()

#Mexico input
def mx():
    #Mexico
    value4 = [dem(i).attr("data-mx-category") for i in dem('.js-est-categories-list .mx-available')]
    value41 = [dem(i).text() for i in dem('.js-est-categories-list .mx-available span')][10]
    value4.append(value41)
    category4 = [dem(i).attr("data-category") for i in dem('.js-est-categories-list .mx-available')]
    mx1 = dict(zip(value4,category4))
    # print(mx1)
mx()

# Italy input
def it():
    #Italy
    value5 = [dem(i).attr("data-it-category") for i in dem('.js-est-categories-list .it-available')]
    value51 = [dem(i).text() for i in dem('.js-est-categories-list .it-available span')][20]
    value5.append(value51)
    category5 = [dem(i).attr("data-category") for i in dem('.js-est-categories-list .it-available')]
    it1 = dict(zip(value5,category5))
    # print(it1)
it()

#Indial input
def In():
    #India1
    value6 = [dem(i).text() for i in dem('.js-est-categories-list .in-available span')]
    value61 = [dem(i).attr("data-in-category") for i in dem('.js-est-categories-list .in-available')]
    v6 = list(filter(None,value61))
    for i in v6:
        value6.append(i)
    category6 = [dem(i).attr("data-category") for i in dem('.js-est-categories-list .in-available')]
    In1 = dict(zip(value6,category6))
    # print(In1)
In()

#Germany input
def de():
    #Germany1...2,4,8,11,12,13,18,27
    value7 = [dem(i).attr("data-de-category") for i in dem('.js-est-categories-list .de-available')]
    value71 = [dem(i).text() for i in dem('.js-est-categories-list .de-available span')]
    value7.append(value71[1])
    value7.append(value71[3])
    value7.append(value71[7])
    value7.append(value71[10])
    value7.append(value71[11])
    value7.append(value71[12])
    value7.append(value71[17])
    value7.append(value71[26])
    v7 = list(filter(None,value7))
    category7 = [dem(i).attr("data-category") for i in dem('.js-est-categories-list .de-available')]
    de1 = dict(zip(v7,category7))
    # print(de1)
de()

#Francel input
def fr():
    #France1
    value8 = [dem(i).attr('data-fr-category') for i in dem('.js-est-categories-list .fr-available')]
    value81 = [dem(j).text() for j in dem('.js-est-categories-list .fr-available span')][7]
    value8.append(value81)
    v8 = list(filter(None,value8))
    category8 = [dem(i).attr('data-category') for i in dem('.js-est-categories-list .fr-available')]
    fr1 = dict(zip(v8,category8))
    # print(fr1)
fr()

#Candal input
def ca():
    #Canada1
    value9 = [dem(i).text() for i in dem('.js-est-categories-list .ca-available span')]
    value91 = [dem(j).attr("data-ca-category") for j in dem('.js-est-categories-list .ca-available') if j != ""]
    v9 = list(filter(None,value91))
    value9.append("".join(v9))
    category9 = [dem(j).attr("data-category") for j in dem('.js-est-categories-list .ca-available')]
    ca1 = dict(zip(value9,category9))
    # print(ca1)
ca()

obj = {}
for i in range(0,len(ids)):
    data = {}  # {id：us,option:{us1}}
    data['id'] = ids[i]
    data['options'] = us()
    obj[arr[i]] = data
print(obj)


with open('country.json', 'w', encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False)

