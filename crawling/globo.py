# -*- coding: utf-8 -*-
import scrapy


class GloboSpider(scrapy.Spider):
    name = 'globo'
    allowed_domains = ['https://www.globo.com']
    start_urls = ['http://https://www.globo.com/']

    def parse(self, response):
        pass
