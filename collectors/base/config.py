# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import logging
import logging.config
from dotenv import load_dotenv
load_dotenv('.env')


# Environment

ENV = os.environ['PYTHON_ENV']
if os.environ.get('CI', None):
    ENV = 'testing'

# Spiders

SPIDER_MODULES = [
    'collectors.actrn.spider',
    'collectors.euctr.spider',
    'collectors.gsk.spider',
    'collectors.ictrp.spider',
    'collectors.isrctn.spider',
    'collectors.jprn.spider',
    'collectors.pfizer.spider',
    'collectors.pubmed.spider',
    'collectors.takeda.spider',
]

# Network

DOWNLOAD_DELAY = float(os.getenv('DOWNLOAD_DELAY', 1))
AUTOTHROTTLE_ENABLED = True

# Pipelines

WAREHOUSE_URL = os.environ['WAREHOUSE_URL']
TEST_WAREHOUSE_URL = os.environ.get('TEST_WAREHOUSE_URL', None)
ITEM_PIPELINES = {
    'collectors.base.pipelines.Warehouse': 100,
}

# Logging


def setup_syslog_handler():
    if os.environ.get('LOGGING_URL', None):
        host, port = os.environ['LOGGING_URL'].split(':')
        handler = logging.handlers.SysLogHandler(address=(host, int(port)))
    else:
        handler = logging.handlers.SysLogHandler()
    return handler


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(name)s: %(message)s',
        },
    },
    'handlers': {
        'default_handler': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'level': 'DEBUG',
            'formatter': 'default'
        },
        'syslog_handler': {
            '()': setup_syslog_handler,
            'level': 'INFO',
            'formatter': 'default',
        },
    },
    'root': {
        'handlers': ['default_handler', 'syslog_handler'],
        'level': os.environ.get('LOGGING_LEVEL', 'DEBUG').upper(),
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

# ICTRP

ICTRP_USER = os.environ.get('ICTRP_USER', None)
ICTRP_PASS = os.environ.get('ICTRP_PASS', None)

# HRA

HRA_ENV = os.environ.get('HRA_ENV', None)
HRA_URL = os.environ.get('HRA_URL', None)
HRA_USER = os.environ.get('HRA_USER', None)
HRA_PASS = os.environ.get('HRA_PASS', None)

# Cochrane Reviews

COCHRANE_ARCHIVE_URL = os.environ.get('COCHRANE_ARCHIVE_URL')
