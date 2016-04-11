# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from dotenv import load_dotenv; load_dotenv('.env')  # noqa


# Spiders

NEWSPIDER_MODULE = 'scraper.spiders'
SPIDER_MODULES = ['scraper.spiders']

# Pipelines

WAREHOUSE_URL = os.environ['OPENTRIALS_WAREHOUSE_URL']
ITEM_PIPELINES = {
    'scraper.pipelines.Database': 100,
}

# Network

DOWNLOAD_DELAY = float(os.getenv('OPENTRIALS_DOWNLOAD_DELAY', 1))
AUTOTHROTTLE_ENABLED = True

# Credentials

ICTRP_USER = os.environ.get('OPENTRIALS_ICTRP_USER', '')
ICTRP_PASS = os.environ.get('OPENTRIALS_ICTRP_PASS', '')
