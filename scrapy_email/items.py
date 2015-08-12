# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyEmailItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    subject = scrapy.Field()
    messageurl = scrapy.Field()
    message = scrapy.Field()
    fromEmail = scrapy.Field()
    toEmail = scrapy.Field()
    date = scrapy.Field()
    attachment = scrapy.Field()
    pass

