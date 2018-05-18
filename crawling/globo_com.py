# -*- coding: utf-8 -*-
import scrapy


class GloboComSpider(scrapy.Spider):
    name = 'globo.com'
    allowed_domains = ['www.globo.com']
    start_urls = ['https://www.globo.com/']

    def parse(self, response):
        print """RODANDO """
        print response

