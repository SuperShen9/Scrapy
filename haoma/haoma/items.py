# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaomaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    provice = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    owner = scrapy.Field()
    type = scrapy.Field()
    post = scrapy.Field()
    pass
