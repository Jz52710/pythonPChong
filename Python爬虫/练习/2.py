# coding:utf-8
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
        headers = {'User_Agent': user_agent}
        try:
            r = requests.get(url, headers=headers)
        except Exception as e:
            print(e)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None