# -*- coding: utf-8 -*-
import scrapy
from moviesA.items import MoviesaItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    index = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = ['http://movie.douban.com/top250?start=0']

    def parse(self, response):
        print(response.xpath('//div[@class = "hd"]'))
    #     for i in response.xpath('//div[@class = "hd"]'):
    #         url = i.xpath("a/@href").extract()[0]
    #         yield scrapy.Request(url,callback=self.parseCon)
    #     self.index += 25
    #     if self.index < 226:
    #         yield scrapy.Request(self.url+str(self.index),callback=self.parse)
    # #详情
    # def parseCon(self,response):
    #     item = MoviesaItem()
    #     item['title'] = response.xpath('//h1/span[1]/text()').extract()[0]
    #     item['directs'] = response.xpath('//div[@id="info"]/span[1]/span[2]/a/text()')[0].extract()
    #     item['actor'] = response.xpath('//span[@class="actor"]/span[2]/a/text()').extract()
    #     item['typ'] = response.xpath('//div[@id="info"]/span[position()>4 and position()<7]/text()').extract()
    #     item['info'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()')[0].extract()
    #     yield item

