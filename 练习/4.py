# coding:utf-8
import codecs, json


class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('news.json', 'w', encoding='utf-8')
        json.dump(self.datas, fp=fout, indent=4, ensure_ascii=False)  # 将所有数据写入文件。