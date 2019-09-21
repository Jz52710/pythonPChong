# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BossPipeline(object):

    def process_item(self, item, spider):
        print(item)
        # import json
        # for udd in item:
        #     # print(udd+':'+item[udd])
        #     # a = dict(udd)
        #     # a = udd+':'+item[udd]
        #     with open('new.json','w', encoding='utf-8') as f:
        #         json.dump(a,f, ensure_ascii=False)
        return item
