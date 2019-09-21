# -*- coding: utf-8 -*-
import scrapy
from BOSS.items import B0SsItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com/']
    start_urls = ['https://www.zhipin.com/c101010100/?page=1']

    def parse(self, response):
        for i in response.xpath('//div[@class="job-primary"]'):
            print(i)
