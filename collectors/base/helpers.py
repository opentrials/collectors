# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import logging
import datetime
logger = logging.getLogger(__name__)


# Module API

def slugify(value):
    """Slugify string value.
    """
    value = re.sub(r'[\W_]+', '_', value)
    value = value.strip('_')
    value = value.lower()
    value = value[:63]  # Postgres limitation is 63
    return value


def parse_date(value, format):
    """Parse sting date.
    """
    return datetime.datetime.strptime(value, format).date()


def parse_datetime(value, format):
    """Parse sting datetime.
    """
    return datetime.datetime.strptime(value, format)


def get_variables(object, filter=None):
    """Exract variables from object to dict using name filter.
    """
    variables = {}
    for name, value in vars(object).items():
        if filter is not None:
            if not filter(name):
                continue
        variables[name] = value
    return variables


def start(conf, name, message):
    """Log collector start.
    """
    logger.info('Collector %s has been started(%s)', name, message)


def stop(conf, name, message):
    """Log collector stop.
    """
    logger.info('Collector %s has stopped (%s)', name, message)
