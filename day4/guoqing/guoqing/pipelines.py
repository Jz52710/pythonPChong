# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class GuoqingPipeline(object):
    def process_item(self, item, spider):
        # imgs = item['image_urls']
        # for i in imgs:
        #     imgss = i.split('/')[-1]
        #     print(imgss)
        return item
