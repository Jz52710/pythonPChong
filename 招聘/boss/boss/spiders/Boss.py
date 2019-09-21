# -*- coding: utf-8 -*-
import scrapy
from boss.items import BossItem

class BossSpider(scrapy.Spider):
    name = 'Boss'
    allowed_domains = ['www.zhaopin.com/']
    url = 'https://www.zhipin.com/c101010100/?page='
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=20&cityId=576']

    def parse(self, response):
        import json
        item = BossItem()
        data = response.text
        # a = json.loads(data)['data']['results'][0]
        a = json.loads(data)['data']['results']
        for i in range(0,len(a)):
            item['title'] = a[i]['jobName']
            item['pay'] = a[i]['salary']
            item['site'] = a[i]['city']['display']
            item['degree'] = a[i]['eduLevel']['name']
            item['company'] = a[i]['company']['name']
            yield item
        # print(a)
        # print(len(a))
        # print(item)
