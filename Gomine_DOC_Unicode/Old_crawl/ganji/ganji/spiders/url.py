# -*- coding: utf-8 -*-
# author:Super
import scrapy
from ganji.items import GanjiItem
from scrapy.http import Request
class ganjispider(scrapy.Spider):
    name = "ganji"
    start_urls = [
        "http://jinhua.ganji.com/xiaoqu/",
    ]


    def parse(self, response):
        for i in range(0, 20,20):
            if i==0:
                detail_url = "http://jinhua.ganji.com/xiaoqu/"
            else:
                detail_url = "http://jinhua.ganji.com/xiaoqu/f" +str(i)+'/'
            req = Request(detail_url, self.parse_url)
            yield req
    def parse_url(self,response):
        for href in response.xpath('//div[@class="info-title"]/a/@href').extract():
            req = Request(href, self.parse_detail)
            yield req

    def parse_detail(self, response):
        names=response.xpath('//div[@class="xiaoqu-top"]/h1/text()').extract()
        prices=response.xpath('//div[@class="basic-info"]/ul/li[1]/b/text()').extract()
        sales=response.xpath('//div[@class="basic-info"]/ul/li[3]/span[4]/a/text()').extract()
        rents = response.xpath('//div[@class="basic-info"]/ul/li[3]/span[2]/a/text()').extract()
        yield GanjiItem(name=names, price=prices,rent=rents,sale=sales)


    # def parse_detail(self, response):
    #     nums=response.xpath('//a[@class="c linkOn"]/span/text()').extract()
    #     xiaoqus = response.xpath('//div[@class="info-title"]/a/text()').extract()
    #     yield GanjiItem(xiaoqu=xiaoqus,num=nums)