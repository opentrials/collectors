# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.crawler import CrawlerProcess
from .spider import IsrctnSpider


def collect(conf, conn, date_from=None, date_to=None):
    process = CrawlerProcess(conf)
    process.crawl(IsrctnSpider,
        conn=conn, date_from=date_from, date_to=date_to)
    process.start()
