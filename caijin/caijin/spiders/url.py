# -*- coding: utf-8 -*-
import scrapy
class caijinSpider(scrapy.Spider):
    name = "caijin"
    start_urls=[
        "https://www.qiushibaike.com/",
    ]
    def parse(self, response):
        print response.xpath('//div[@class="content"]').extract()
