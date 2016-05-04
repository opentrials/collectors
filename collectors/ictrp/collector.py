# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.crawler import CrawlerProcess
from .spider import IctrpSpider


def collect(conf, conn):
    process = CrawlerProcess(conf)
    process.crawl(IctrpSpider,
        conn=conn, http_user=conf['ICTRP_USER'], http_pass=conf['ICTRP_PASS'])
    process.start()
