# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean


# Module API

class Record(base.Record):

    # Config

    table = 'icdpcs'
    primary_key = 'code'
    updated_key = 'last_updated'
    ensure_fields = False

    # General

    code = Text()
    is_header = Boolean('0')
    short_description = Text()
    long_description = Text()
    version = Text()
    last_updated = Date('%Y-%m-%d')
