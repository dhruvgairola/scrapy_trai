# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_email project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_email'

SPIDER_MODULES = ['scrapy_email.spiders']
NEWSPIDER_MODULE = 'scrapy_email.spiders'

ITEM_PIPELINES = { 'scrapy_email.pipelines.ScrapyEmailPipeline': 800,}
# DOWNLOAD_DELAY = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_email (+http://www.yourdomain.com)'
