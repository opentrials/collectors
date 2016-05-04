# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from datetime import datetime


# Module API

def slugify(name):
    """Replace unwanted chars.
    """
    name = name.lower()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[^\w]+', '', name)
    name = '_'.join(name.split('_')[:8])
    return name


def parse_date(value, format):
    """Parse sting date.
    """
    return datetime.strptime(value, format).date()


def parse_datetime(value, format):
    """Parse sting datetime.
    """
    return datetime.strptime(value, format)
