import urlparse
import scrapy
from scrapy import Request
from scrapy_email.items import ScrapyEmailItem
from math import sin, cos, sqrt, atan2, radians

class ScrapyEmailSpider(scrapy.Spider):
    name = "email"
    allowed_domains = ["trai.gov.in"]

    # db = mysqldb.connect(host="localhost", # your host, usually localhost
    #                  user="root", # your username
    #                   passwd="", # your password
    #                   db="test") # name of the data base
    # cur = db.cursor() 

    start_urls = [
        'http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/27-mar.html',
        'http://trai.gov.in/Comments/11-APRIL/11-April.html',
        'http://www.trai.gov.in/Comments/12-April/12-April-p2/12-April-p2.html',
        'http://www.trai.gov.in/Comments/13-April/html-13/13-April/p1/13-April.html',
        'http://www.trai.gov.in/Comments/14-April-1/14-April-1.html',
        'http://www.trai.gov.in/Comments/14-April-2/14-April-2.html',
        'http://www.trai.gov.in/Comments/14-April-3/14-April-3.html',
        'http://www.trai.gov.in/Comments/14-April-4/14-April-4.html',
        'http://www.trai.gov.in/Comments/16-April/16-April/16-April.html',
        'http://www.trai.gov.in/Comments/16-April/16-April-p2/16-April-p2.html',
        'http://trai.gov.in/Comments/17-April/17-April.html',
        'http://trai.gov.in/Comments/18-April/18-April.html',
        'http://trai.gov.in/Comments/19-April/19-April.html',
        'http://trai.gov.in/comments/20-April/20-April.html',
        'http://www.trai.gov.in/Comments/21-April/21-April.html',
        'http://www.trai.gov.in/Comments/22-April/22-April.html',
        'http://trai.gov.in/comments/OLD/23-April/23-April.html',
        'http://trai.gov.in/comments/24-April/24-April.html'
    ]

    start_urls_chopped = [
        'http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/',
        'http://trai.gov.in/Comments/11-APRIL/',
        'http://www.trai.gov.in/Comments/12-April/12-April-p2/',
        'http://www.trai.gov.in/Comments/13-April/html-13/13-April/p1/',
        'http://www.trai.gov.in/Comments/14-April-1/',
        'http://www.trai.gov.in/Comments/14-April-2/',
        'http://www.trai.gov.in/Comments/14-April-3/',
        'http://www.trai.gov.in/Comments/14-April-4/',
        'http://www.trai.gov.in/Comments/16-April/16-April/',
        'http://www.trai.gov.in/Comments/16-April/16-April-p2/',
        'http://trai.gov.in/Comments/17-April/',
        'http://trai.gov.in/Comments/18-April/',
        'http://trai.gov.in/Comments/19-April/',
        'http://trai.gov.in/comments/20-April/',
        'http://www.trai.gov.in/Comments/21-April/',
        'http://www.trai.gov.in/Comments/22-April/',
        'http://trai.gov.in/comments/OLD/23-April/',
        'http://trai.gov.in/comments/24-April/'
    ]
    # start_urls = [
    #     'http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/27-mar.html'
    # ]
    
    # start_urls_chopped = [
    #     'http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/'
    # ]

    def __init__(self):
        print("Initializing...")

    def start_requests(self):
        for indx, val in enumerate(self.start_urls):
            yield self.make_requests_from_url(val, {'index': indx})

    def make_requests_from_url(self, url, meta):
       return Request(url, callback=self.parse, dont_filter=True, meta=meta)

    def parse(self, response):
        
        for sel in response.xpath('//tr'):
            link = sel.xpath('./td/a/@href')
            msgLink = ""

            if link:
                msgLink = link[0].extract().strip()
            
            baseUrl = self.start_urls_chopped[int(response.meta['index'])]
            item = ScrapyEmailItem()
            item['messageurl'] = baseUrl + msgLink

            subj = sel.xpath('./td/a/text()')
            
            if subj:
                item['subject'] = subj[0].extract().strip()

            details = sel.xpath('./td/text()')

            if not details:
                continue

            nameAndEmail = details[0].extract().strip()
            
            fromEmail = ""
            if nameAndEmail:
                ne = nameAndEmail.split("<")
                if len(ne) == 1:
                    fromEmail = ne[0].strip()
                elif len(ne) == 2:
                    name = ne[0].strip()
                    item['name'] = name
                    fromEmail = ne[1].strip()
                
                if fromEmail:
                    fromEmail = fromEmail[:-1]
                    fromEmail = fromEmail.replace("(dot)", ".")
                    fromEmail = fromEmail.replace("(at)", "@")
                    item['fromEmail'] = fromEmail
            
            if not fromEmail:
                continue;

            if len(details)>1:
                toEmail = details[1].extract().strip()
                
            if toEmail:
                toEmail = toEmail.replace("(dot)", ".")
                toEmail = toEmail.replace("(at)", "@")
                item['toEmail'] = toEmail
            
            if len(details)>2:
                item['date'] = details[2].extract().strip()
            # print item
            yield Request(item['messageurl'], meta={'item': item}, callback=self.parse_email_msg) 


    def parse_email_msg(self, response):
        item = response.request.meta['item']
        
        msg = ""
        for sel in response.xpath('//div'):
            msg = msg + sel.extract().encode('utf-8')

        if not msg:
            msg = response.xpath('.').extract()

        item['message'] = msg

        yield item