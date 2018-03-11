# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeixiaohaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    liutong_value = scrapy.Field()
    global_pro = scrapy.Field()
    liutong_rate = scrapy.Field()
    huanshou_rate = scrapy.Field()
    price_change =scrapy.Field()
    pass
