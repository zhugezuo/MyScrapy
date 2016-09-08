# -*- coding: UTF-8 -*-
import scrapy
from Scrapy.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # 生成item
    def parse(self, response):
        for sel in response.xpath("//div[@class='title-and-desc']"):
            item = DmozItem()
            item['title'] = sel.xpath("a/div[@class='site-title']/text()").extract()
            item['link'] = sel.xpath("a/@href").extract()
            item['desc'] = sel.xpath("div[@class='site-descr ']/text()").extract()
            yield item
