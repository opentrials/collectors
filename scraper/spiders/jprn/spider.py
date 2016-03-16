# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from six.moves.urllib.parse import urlparse, parse_qs

from .. import base
from . import utils
from .mapper import JprnMapper


# Module API

class JprnSpider(base.Spider):

    # Public

    name = 'jprn'
    allowed_domains = ['upload.umin.ac.jp']

    def __init__(self, page_from=None, page_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = JprnMapper()

        # Default values
        if page_from is None:
            page_from = '1'
        if page_to is None:
            page_to = '1'

        # Save attributes
        self.__page_from = page_from
        self.__page_to = page_to

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='https://upload.umin.ac.jp/cgi-open-bin/ctr/ctr.cgi',
                page_from=page_from)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'cgi-open-bin/ctr/ctr.cgi\?function=brows',
            ), callback=self.mapper.map_response),
            Rule(LinkExtractor(
                allow=r'page=\d+',
                process_value=self.process_url,
            )),
        ]

        # Inherit parent
        super(JprnSpider, self).__init__(*args, **kwargs)

    def process_url(self, url):

        # Get url page
        query = urlparse(url).query
        query = parse_qs(query)
        page = query.get('_page')

        # Preserve if match
        if page:
            page_from = int(self.__page_from)
            page_to = int(self.__page_to)
            page = int(page[0])
            if page >= page_from and page <= page_to:
                return url

        return None
