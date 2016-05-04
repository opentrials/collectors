# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.crawler import CrawlerProcess
from .spider import JprnSpider


def collect(conf, conn, page_from=None, page_to=None):
    process = CrawlerProcess(conf)
    process.crawl(JprnSpider,
        conn=conn, page_from=page_from, page_to=page_to)
    process.start()
