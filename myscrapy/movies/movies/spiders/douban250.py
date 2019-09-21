# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem


class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        # dy = []
        # dao = []
        # title =response.xpath('//span[@class="title"][1]/text()').extract()
        # dirss = response.xpath('//div[@class = "bd"]/p[1]/text()').extract()
        # for i in dirss:
        #     a = ''.join(i).strip()
        #     b = a.split('\xa0\xa0\xa0')
        #     dy.append(b)
        # for j in range(0,len(dy),2):
        #     d = dy[j][0]
        #     dao.append(d)
        # dirs = dao
        # info = response.xpath('//span[@class="rating_num"]/text()').extract()
        # scour = response.xpath('//span[@class="inq"]/text()').extract()
        # print(title)
        # print(dirs)
        # print(info)
        # print(scour)
        for i in response.xpath('//div[@class="item"]'):
            item =MoviesItem()
            item['title'] = i.xpath('div[@class="info"]/div/a/span[1]/text()')[0].extract()
            item['dirs'] = i.xpath('div[@class="info"]/div[@class="bd"]/p[1]/text()')[0].extract().strip()
            item['info'] = i.xpath('div[@class="info"]/div[@class="bd"]/div/span[2]/text()')[0].extract()
            item['scour'] = i.xpath('div[@class="info"]/div[@class="bd"]/p[2]/span/text()')[0].extract()
            yield item