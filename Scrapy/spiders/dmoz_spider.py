import scrapy

from Scrapy.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # 追踪链接
    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    # 生成item
    def parse_dir_contents(self, response):
        for sel in response.xpath("/html/body/div[@id='main-content']/div[@id='doc']/section[@class='results sites']/div[@id='sites-section']/div[@id='site-list-content']"):
            item = DmozItem()
            item['title'] = sel.xpath("//div[@class='title-and-desc']/a/div[@class='site-title']/text()").extract()
            item['link'] = sel.xpath("//div[@class='title-and-desc']/a/@href").extract()
            item['desc'] = sel.xpath("//div[@class='title-and-desc']/div[@class='site-descr ']/text()").extract()
            yield item
