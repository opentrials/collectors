# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date


# Module API

class Record(base.Record):

    # Config

    table = 'fdadl'
    primary_key = 'product_ndc'
    ensure_fields = False

    # General

    product_ndc = Text()
    product_type = Text()
    generic_name = Text()
    brand_name = Text()
    last_updated = Date('%Y-%m-%d')
