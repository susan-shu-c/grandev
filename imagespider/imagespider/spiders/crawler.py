from imagespider.items import ImagespiderItem
import datetime
import scrapy

class Crawler(scrapy.Spider):
    name = "image_spider"
    pages = 0
    start_urls = ["https://www.gettyimages.ca/photos/ariana-grande?family=editorial&phrase=ariana%20grande&sort=best#license"]

    def parse(self, response):
        Crawler.pages+=1
        url = response.xpath('//*[@id="assets"]/article')
        data = url.xpath('//*[@id="assets"]/article').extract()

        for href in data:
            imglink = href[href.find('src'):]
            imglink = imglink[5:imglink.find('>')-1]
            title = href[href.find('target'):]
            title = title[8:title.find('>')-1]
            now = datetime.datetime.now()
            yield ImagespiderItem(title=title, createDate=now, image_urls=[imglink])

        if Crawler.pages !=2:
            next = response.xpath('//*[@id="next-gallery-page"]')
            if next is not None:
                yield scrapy.Request("https://www.gettyimages.com"+next.xpath("@href").extract_first(), self.parse)
