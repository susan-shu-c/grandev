from imagespider.items import ImagespiderItem
import datetime
import scrapy

class Crawler(scrapy.Spider):
    name = "image_spider2"
    pages = 0
    start_urls = ["https://www.gettyimages.ca/photos/ariana-grande?family=editorial&phrase=ariana%20grande&sort=best#license"]

    def parse(self, response):
        # Crawler.pages+=1
        # url = response.xpath('//*[@id="assets"]/article')
        data = response.css('img').xpath('@src').getall() # this should be list of urls (string)

        for href in data:
            title = data.index(href) # The element in list
            imglink = href
            now = datetime.datetime.now()
            yield ImagespiderItem(title=title, createDate=now, image_urls=[imglink])

        # if Crawler.pages !=2:
            # next = response.xpath('//*[@id="next-gallery-page"]')
            # if next is not None:
                # yield scrapy.Request("https://www.gettyimages.com"+next.xpath("@href").extract_first(), self.parse)
