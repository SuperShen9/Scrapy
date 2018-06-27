# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # xiaoqu = scrapy.Field()
    # num=scrapy.Field()
    name= scrapy.Field()
    price= scrapy.Field()
    rent= scrapy.Field()
    sale=scrapy.Field()
    pass
