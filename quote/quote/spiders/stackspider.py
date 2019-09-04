from scrapy import Spider
from scrapy.selector import Selector

from ..items import StackItems


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["sinta2.ristekdikti.go.id"]
    start_urls = ["http://sinta2.ristekdikti.go.id/affiliations/detail?page=2&id=384&view=documents&q=smart%20city&search=1",]

    def parse(self, response):
        questions = Selector(response).xpath('//dt[@class="uk-text-primary"]')

        for question in questions:
            item = StackItems()
            item['title'] = question.xpath(
                'a[@class="paper-link"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="paper-link"]/@href').extract()[0]
            yield item