# -*- coding: utf-8 -*-
import scrapy

class zhihuspider(scrapy.Spider):
    name = "zhihu"
    start_urls = [
        "https://www.zhihu.com/#signin",
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"email":'675153178@qq.com',"password":'scrapyzhihu9339'},
            callback=self.after_login,
            method="POST",
            url="https://www.zhihu.com/login/email")

    def after_login(self,response):
        print response.body

