# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from shutterstock.items import ShutterstockItem

class WallsSpider(Spider):
    name = 'walls'
    allowed_domains = ['shutterstock.com']
    start_urls = ['http://shutterstock.com/']

    def __init__(self, query):
        self.start_urls = [r'https://shutterstock.com/search/'+query]
        # self.page = page

    def parse(self, response):
        sel = response.xpath("//img[@class='z_e_h']")
        img_urls = sel.xpath(".//@src").extract()
        names = sel.xpath(".//@alt").extract()
        l = ItemLoader(item=ShutterstockItem(), response=response)
        for url, name in zip(img_urls, names):
            l.add_value('name', name)
            l.add_value('img_urls', img_urls)
            yield {
            'Image URL' : url,
            'Name' : name,
            'image_urls' : [url],
            }


        next_page_url = response.urljoin(response.xpath("//a[@data-automation='BottomNav_NextButton']/@href").extract_first())
        yield Request(next_page_url)
        # l.add_value('name', name)
        # l.add_value('img_urls', img_urls)

        return l.load_item()






