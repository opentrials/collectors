# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

import scrapy
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
#from .parser import parse_record


class EpistemonikosSpider(CrawlSpider):
    name = 'epistemonikos'
    allowed_domains = ['api.epistemonikos.org']

    def __init__(self, conf=None, conn=None):
        self.conf = conf
        self.conn = conn

        self.start_urls = [
            'https://api.epistemonikos.org/v1/documents/search?q=*&show=classification',
        ]

        super(EpistemonikosSpider, self).__init__()

    def make_requests_from_url(self, url, callback=None):
        TOKEN = self.conf['EPISTEMONIKOS_TOKEN']
        headers = {
            'Authorization': 'Token token="{token}"'.format(token=TOKEN),
        }
        return Request(url, callback=callback or self.parse, headers=headers)

    def parse_start_url(self, response):
        BASE_URL = 'https://api.epistemonikos.org'
        result = json.loads(response.body)
        next_link = result['search_info']['pages'].get('last')

        for document in result['results']:
            if document['classification'] == 'systematic-review':
                url = BASE_URL + document['document_uri']
                yield self.make_requests_from_url(url, callback=self.parse_item)

        if next_link:
            # FIXME: Their links don't add "classification"
            url = BASE_URL + next_link + '&show=classification'
            yield self.make_requests_from_url(url)

    def parse_item(self, response):
        import pdb
        pdb.set_trace()
        pass


class JSONLinkExtractor(LinkExtractor):
    def extract_links(self, response):
        print("EXTRACT LINKS")
        import pdb
        pdb.set_trace()
