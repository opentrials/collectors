# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import logging
from logging.handlers import SysLogHandler
from dotenv import load_dotenv
load_dotenv('.env')


# Environment

ENV = os.environ['PYTHON_ENV']

# Spiders

SPIDER_MODULES = [
    'collectors.actrn.spider',
    'collectors.euctr.spider',
    'collectors.gsk.spider',
    'collectors.ictrp.spider',
    'collectors.isrctn.spider',
    'collectors.jprn.spider',
    'collectors.nct.spider',
    'collectors.pfizer.spider',
    'collectors.pubmed.spider',
    'collectors.takeda.spider',
]

# Network

DOWNLOAD_DELAY = float(os.getenv('DOWNLOAD_DELAY', 1))
AUTOTHROTTLE_ENABLED = True

# Pipelines

WAREHOUSE_URL = os.environ['WAREHOUSE_URL']
ITEM_PIPELINES = {
    'collectors.base.pipelines.Warehouse': 100,
}

# Logging

logging.basicConfig(level=logging.DEBUG)
if os.environ.get('LOGGING_URL', None):
    root_logger = logging.getLogger()
    host, port = os.environ['LOGGING_URL'].split(':')
    syslog_handler = SysLogHandler(address=(host, int(port)))
    syslog_handler.setLevel(logging.INFO)
    root_logger.addHandler(syslog_handler)

# ICTRP

ICTRP_USER = os.environ.get('ICTRP_USER', None)
ICTRP_PASS = os.environ.get('ICTRP_PASS', None)

# HRA

HRA_ENV = os.environ.get('HRA_ENV', None)
HRA_URL = os.environ.get('HRA_URL', None)
HRA_USER = os.environ.get('HRA_USER', None)
HRA_PASS = os.environ.get('HRA_PASS', None)
