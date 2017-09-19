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
    def parse(self, response):
        for i in range(1, 14):
            if i==1:
                detail_url = "https://www.qiushibaike.com/"
            else:
                detail_url = "https://www.qiushibaike.com/8hr/page/" +str(i)+'/'
            req = Request(detail_url, self.parse_url)
            yield req

    def parse_url(self, response):
        for href in response.xpath('//span[@class="stats-comments"]/a/@href').extract():
            comm_urls = response.urljoin(href)
            req = Request(comm_urls, self.parse_detail)
            item = CaijinItem()
            req.meta["item"] = item
            yield req

    def parse_detail(self, response):
        item = response.meta["item"]
        if len(response.xpath('//div[@class="author clearfix"]/a[2]/h2/text()').extract()) == 0:
            item["author"] = ""
        else:
            item["author"] = response.xpath('//div[@class="author clearfix"]/a[2]/h2/text()').extract()[0]
        if len(response.xpath('//div[@class="content"]/text()').extract()) == 0:
            item["content"] = ''
        else:
            item["content"] = response.xpath('//div[@class="content"]/text()').extract()[0]
        comments = []
        for comment in response.xpath('//div[starts-with(@class,"comment-block clearfix")]'):
            if len(comment.xpath('./div[2]/a/text()').extract()) == 0:
                comment_author = ''
            else:
                comment_author = comment.xpath('./div[2]/a/text()').extract()[0]

            if len(comment.xpath('./div[2]/span/text()').extract()) == 0:
                comment_content = ''
            else:
                comment_content = comment.xpath('./div[2]/span/text()').extract()[0]
            comments.append({"comment_author": comment_author, "comment_content": comment_content})
        item["comments"] = comments
        yield item



# -------------抓取所有页面的笑话----------------------------------------------
#     def parse(self, response):
#         for i in range(1, 14):
#             if i==1:
#                 detail_url = "https://www.qiushibaike.com/"
#             else:
#                 detail_url = "https://www.qiushibaike.com/8hr/page/" +str(i)+'/'
#             req = Request(detail_url, self.parse_next)
#             yield req
#             print detail_url
#     def parse_next(self, response):
#         for ele in response.xpath('//div[starts-with(@class,"article block untagged mb15")]'):
#             authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
#             contents = ele.xpath('.//div[@class="content"]/span/text()').extract()
#             yield CaijinItem(author=authors, content=contents)