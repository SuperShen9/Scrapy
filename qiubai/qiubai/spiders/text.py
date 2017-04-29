# -*- coding: utf-8 -*-
import scrapy
class qiubaispider (scrapy.Spider):
    name="text"
    start_urls=[
        "http://www.qiushibaike.com/users/30998801/",
        "http://www.qiushibaike.com/users/30789405/",
        "http://www.qiushibaike.com/users/10514968/"
    ]
    flag = False
    def parse(self,response):
        if not self.flag:
            self.flag=True
            from scrapy.shell import inspect_response
            inspect_response(response, self)
