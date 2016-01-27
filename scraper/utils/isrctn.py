# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime


# Module API

def parse_date(value):
    return datetime.strptime(value, '%d/%m/%Y').date()
