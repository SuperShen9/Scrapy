# -*- coding: utf-8 -*-
# author:Super
import scrapy
from scrapy.http import Request
from shiye.items import ShiyeItem
class shiyespider(scrapy.Spider):
    name = "shiye"
    start_urls = [
        "http://search.gjsy.gov.cn:9090/queryAll/searchFrame?districtCode=632121&checkYear=2016&sydwName=18",
    ]


    def parse(self,response):
        for body in response.xpath('//tr[@class="STYLE19"]'):
            urls= body.xpath('./td[2]/a/@href').extract()
            codes= body.xpath('./td[2]/a/text()').extract()
            names= body.xpath('./td[3]/a/text()').extract()
            yield ShiyeItem(url=urls,code=codes,name=names)
        # for href in response.xpath('//tr[@class="STYLE19"]/td[2]/a/@href').extract():
        #     print response.urljoin(href)
            # print response.xpath('//tr[@class="STYLE19"]/td[2]/a/text()').extract()
            # print response.xpath('//tr[@class="STYLE19"]/td[3]/a/text()').extract()
