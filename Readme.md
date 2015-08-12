This project scrapes the emails available on a couple of publicly available url's on TRAI's (Telecom Regulatory Authority of India) website. Takes a really long time to run because the email contents are being scraped too.

#### Installation steps :
```
1. Install the following packages:
> pip install Scrapy
> pip install service_identity
```

#### Additional configuration :

To scrape, run this command from the top level directory.
```
> scrapy crawl email -o emails.csv
```