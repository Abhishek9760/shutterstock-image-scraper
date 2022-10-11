# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# this is something very important that i am about to tell
#do not skip https://doc.scrapy.org/en/latest/topics/items.html 
#read very carefully thx:)
import scrapy


class ShutterstockItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    img_urls = scrapy.Field()
    images = scrapy.Field()
