from scrapy.spider import Spider
class FirstSpider(Spider):
    name = "first"
    allowed_domain =["baidu.com"]
    start_urls = ["http://www.baidu.com",]
    def parse(self,response):
        pass
 
