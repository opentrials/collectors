# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


# Spiders

NEWSPIDER_MODULE = 'scraper.spiders'
SPIDER_MODULES = [
    'scraper.spiders.ctgov.spider',
    'scraper.spiders.isrctn.spider',
]

# Pipelines

DATABASE_URL = os.environ['OPENTRIALS_DATABASE_URL']
ITEM_PIPELINES = {
    'scraper.pipelines.database.Database': 100,
}

# Network

DOWNLOAD_DELAY = float(os.getenv('OPENTRIALS_DOWNLOAD_DELAY', 1))
AUTOTHROTTLE_ENABLED = True
