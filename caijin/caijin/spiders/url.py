# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from caijin.items import CaijinItem

class caijinSpider(scrapy.Spider):
    name = "caijin"
    start_urls=[
        "https://www.qiushibaike.com/",
    ]

    # def parse(self, response):
    #     print response.xpath('//div[@class="content"]').extract()


    # def parse(self, response):
    #     extract=LinkExtractor(allow="/8hr/page/*")
    #     links=extract.extract_links(response)
    #     for link in links:
    #         yield Request(link.url,self.parse_next)




# -------------抓取所有页面的笑话----------------------------------------------
    def parse(self, response):
        for i in range(1, 14):
            detail_url = "https://www.qiushibaike.com/8hr/page/" +str(i)+'/'
            req = Request(detail_url, self.parse_next)
            yield req
            print detail_url
    def parse_next(self, response):
        for ele in response.xpath('//div[starts-with(@class,"article block untagged mb15")]'):
            authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            contents = ele.xpath('.//div[@class="content"]/span/text()').extract()
            yield CaijinItem(author=authors, content=contents)