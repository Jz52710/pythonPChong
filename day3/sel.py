from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from urllib.request import urlopen,Request
import lxml.etree as et

driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

driver.get('https://accounts.douban.com/passport/login_popup?login_source=anony')
time.sleep(3)
#创建事件对象
action = ActionChains(driver)
#获取
login = driver.find_element_by_class_name("account-tab-account")
action.click(login).perform()

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys('18634688517')
password.send_keys('jz52710')

logon = driver.find_element_by_link_text("登录豆瓣")
action.click(logon).perform()
time.sleep(3)

urls = ["https://movie.douban.com/subject/26794435/comments?start=%s&limit=20&sort=new_score&status=P"%i for i in range(0,481,20)]
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
url1 = Request(urls,headers=headers)
index =0
for url in urls:
    index+=1
    driver.get(url)
    time.sleep(3)
    # data =driver.page_source
    data = driver.find_elements_by_xpath('//span[@class="short"]/text()')

    # re = urlopen(url).read().decode()
    # hemlObj = et.HTML(re)
    # yp = hemlObj.xpath('//span[@class="short"]/text()')
    # print(data)

    # with open("豆瓣登录爬/%s.html"%index,'w',encoding='utf-8') as f:
    #     f.write(data)
    print(data)
driver.close()
