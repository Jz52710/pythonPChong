# coding:utf-8
import re
import urllib
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url:下载页面的URL
        :param html_cont:下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的URL集合
        :param page_url:下载页面的URL
        :param soup:soup
        :return:返回新的URL集合
        '''
        new_urls = set()
        # 抽取符合要求的a标记
        links = soup.find_all('a', href=re.compile(r'http://news.+\.shtml'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接成完整网址
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''抽取有效数据
        :param page_url:下载页面的URL
        :param soup：soup
        :return:返回有效数据
        '''
        try:
            data = {}
            print('抓取' + str(page_url))
            data['url'] = page_url
            title = soup.find('h1', {'id': 'artical_topic'}).text
            data['title'] = title
            summary = soup.find('div', {'id': 'main_content'}).text
            # 获取tag中包含的所有新闻文本内容，将结果作为Unicode字符串返回
            data['summary'] = summary
            return data
        except:
            print("链接不符合")
            return None