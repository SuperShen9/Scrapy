# -*- coding: utf-8 -*-
import scrapy
class qiubaispider (scrapy.Spider):
    name="qiubai"
    start_urls=[
        "http://www.qiushibaike.com/",
    ]
    def parse(self,response):
        print response.xpath('//div[@class="content"]').extract()

