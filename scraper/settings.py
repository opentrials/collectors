# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


# Spiders

NEWSPIDER_MODULE = 'scraper.spiders'
SPIDER_MODULES = [
    'scraper.spiders.actrn',
    'scraper.spiders.euctr',
    'scraper.spiders.gsk',
    'scraper.spiders.isrctn',
    'scraper.spiders.jprn',
    'scraper.spiders.nct',
]

# Pipelines

WAREHOUSE_URL = os.environ['OPENTRIALS_WAREHOUSE_URL']
ITEM_PIPELINES = {
    'scraper.pipelines.Database': 100,
}

# Network

DOWNLOAD_DELAY = float(os.getenv('OPENTRIALS_DOWNLOAD_DELAY', 1))
AUTOTHROTTLE_ENABLED = True
