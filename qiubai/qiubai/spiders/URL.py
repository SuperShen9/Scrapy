# -*- coding: utf-8 -*-
import scrapy

from qiubai.items import QiubaiItem

class qiubaispider (scrapy.Spider):
    name="qiubai"
    start_urls=[
        "http://www.qiushibaike.com/",
    ]
    def parse(self,response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        for ele in response.xpath('//div[@class="article block untagged mb15"]'):
            authors=ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            contents = ele.xpath('.//div[@class="content"]/span/text()').extract()
            yield QiubaiItem(author=authors,content=contents)

