# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Integer, Json


# Module API

class Record(base.Record):

    # Config

    table = 'fda_dap'

    # General

    id = Text(primary_key=True)
    fda_application_num = Text()
    supplement_number = Integer()
    action_date = Date('%m/%d/%Y')
    approval_type = Text()
    notes = Text()
    documents = Json()
