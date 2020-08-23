import scrapy
import time


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        self.log("Printed immediately.")
        time.sleep(7.2)
        self.log("Printed after 7.2 seconds.")
        filename = 'quotes-%s.html' % page
        self.log('Saved file is %s' % filename)
