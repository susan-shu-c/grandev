from imagespider.items import ImagespiderItem
import datetime
import scrapy

class Crawler(scrapy.Spider):
    name = "image_spider2_non_ari"
    pages = 0 
    page_limit = 10 # pages to scrape
    start_urls = ["https://www.gettyimages.ca/search/2/image?family=editorial&phrase=&sort=mostpopular#license"]

    def parse(self, response):
        Crawler.pages+=1

        data = response.css('img').xpath('@src').getall() # this should be list of urls (string)

        for href in data:
            title = data.index(href) # The element in list
            imglink = href
            now = datetime.datetime.now()
            yield ImagespiderItem(title=title, createDate=now, image_urls=[imglink])

        if Crawler.pages < Crawler.page_limit:
            yield scrapy.Request("https://www.gettyimages.ca/search/2/image?family=editorial&page=" + str(Crawler.pages) + "&phrase=&sort=mostpopular#license", self.parse)

