# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from datetime import datetime


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
    return datetime.strptime(value, format).date()


def parse_datetime(value, format):
    """Parse sting datetime.
    """
    return datetime.strptime(value, format)
