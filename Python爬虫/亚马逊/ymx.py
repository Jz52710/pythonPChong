from selenium import webdriver
import time
import json

class updata:
    def __init__(self):
        self.data = []
        self.imgs = []
        self.inputs = input('请输入关键字:')
        self.urls = 'https://www.amazon.com/s?k=%s&page=1&__mk_zh_CN=亚马逊&qid=1568718182&ref=sr_pg_2'%self.inputs
    def run(self):
        driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver.get(url=self.urls)
        time.sleep(5)
        #图片
        imgg = driver.find_elements_by_class_name('s-image')
        for i in imgg:
            res = i.get_attribute('src')
            self.data.append(res)
            # print(res)
            print("正在下载%s"%res)
            # print(res.split('/')[-1])
            # # print(fileimg)
            # with open('image/'+res.split('/')[-1],'wb') as f:
            #     f.write(res.split('/')[-1])
        #名称
        names = driver.find_elements_by_class_name('a-size-base-plus')
        for j in names:
            name = j.text
            # self.data['name'] = name
            self.data.append(name)
            # print(name)
        #价格
        prices = driver.find_elements_by_xpath('//span[@class="a-price"]')
        for k in prices:
            price = k.text
            abb = price.split('\n')
            jg = ".".join(abb)
            # self.data['price'] = jg
            self.data.append(jg)
            # print(jg)
        driver.close()
    def save(self):
        print(self.data)
        # print(self.imgs)
        with open('shopping.txt', 'w', encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False)

g = updata()
g.run()
g.save()