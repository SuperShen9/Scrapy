# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from haoma.items import HaomaItem
class haomaspider(scrapy.Spider):
    name = "haoma"
    start_urls = [
        "http://www.guisd.com/",
    ]

    def parse(self, response):
        for url1 in response.xpath('//dd/a/@href').extract():
            req=Request(response.urljoin(url1),self.parse_2)
            yield req

    def parse_2(self,response):
        for url2 in response.xpath('//dd/a/@href').extract():
            print response.urljoin(url2)
            req2=Request(response.urljoin(url2),self.parse_3)
            yield req2

    def parse_3(self, response):
        for tr in response.xpath('//tr'):
            nums = tr.xpath('./td/a/text()').extract()
            provices = tr.xpath('./td[2]/text()').extract()
            citys =  tr.xpath('./td[3]/text()').extract()
            areas =  tr.xpath('./td[4]/text()').extract()
            posts =  tr.xpath('./td[5]/text()').extract()
            owners = tr.xpath('./td[6]/text()').extract()
            types =  tr.xpath('./td[7]/text()').extract()
            yield HaomaItem(num=nums,provice=provices,city=citys,
                            area=areas,owner=owners,type=types,post=posts)







