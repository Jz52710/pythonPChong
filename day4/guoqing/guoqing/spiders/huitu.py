# -*- coding: utf-8 -*-
import scrapy
from guoqing.items import GuoqingItem

class HuituSpider(scrapy.Spider):
    name = 'huitu'
    allowed_domains = ['soso.huitu.com']
    start_urls = ['http://soso.huitu.com/search?kw=宇宙']

    def parse(self, response):
        imgs = response.xpath('//div[@class="seozone"]/a/img/@originalsrc').extract()
        for url in imgs:
            item = GuoqingItem()
            item['image_urls'] = [url]
            yield item
