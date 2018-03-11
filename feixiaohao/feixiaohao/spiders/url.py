# -*- coding: utf-8 -*-
import scrapy
from feixiaohao.items import FeixiaohaoItem
from scrapy.http import Request

class fxhspider(scrapy.Spider):
    name = "fxh"
    start_urls = [
        "https://www.feixiaohao.com/currencies/",
    ]

    def parse(self, response):
        for i in range(1, 2):
            if i==1:
                detail_url = "https://www.feixiaohao.com/currencies/"
            else:
                detail_url = "https://www.feixiaohao.com/currencies/list_" +str(i)+'.html'
            req = Request(detail_url, self.parse_url)
            yield req

    def parse_url(self,response):
        for href in response.xpath('//div[@class="boxContain"]//tr/td[2]/a/@href').extract():
            d_url=response.urljoin(href)
            req = Request(d_url, self.parse_detail)
            yield req

    def parse_detail(self, response):
        names = response.xpath('//div[@class="firstPart"]/div/h1/text()').extract()[1]
        prices = response.xpath('//div[@class="firstPart"]/div/div[@class="coinprice"]/text()').extract()[0]
        liutong_values = response.xpath('//div[@class="firstPart"]/div[2]/div[@class="value"]/text()').extract()[0]
        global_pros= response.xpath('//div[@class="firstPart"]/div[2]//div[@class="chardec"]/span/text()').extract()
        liutong_rates = response.xpath('//div[@class="firstPart"]/div[3]//div[@class="chardec"]/span/text()').extract()
        huanshou_rates = response.xpath('//div[@class="firstPart"]/div[4]//div[@class="chardec"]/span/text()').extract()
        price_changes= response.xpath('//div[@class="firstPart"]/div/div[@class="coinprice"]/span/text()').extract()
        yield FeixiaohaoItem(name=names, price=prices, liutong_value=liutong_values,
                             global_pro=global_pros,liutong_rate=liutong_rates,
                             huanshou_rate=huanshou_rates,price_change=price_changes)