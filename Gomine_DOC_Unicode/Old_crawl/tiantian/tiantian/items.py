# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiantianItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    time = scrapy.Field()
    company = scrapy.Field()
    num = scrapy.Field()
    per = scrapy.Field()
    introduce = scrapy.Field()
    pass
