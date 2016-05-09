# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Array


# Module API

class Record(base.Record):

    # Config

    table = 'icdcm'
    primary_key = 'name'
    updated_key = 'last_updated'
    ensure_fields = False

    # General

    name = Text()
    desc = Text()
    terms = Array()
    version = Text()
    last_updated = Date('%Y-%m-%d')
