# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyEmailPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    # def process_item(self, item, spider):
    	# print "Processing."
    	# return item
        # if(item['url'] in self.ids_seen):
        #     print "Rejected item."
        # else:
        # 	self.ids_seen.add(item['url'])
        # 	return item