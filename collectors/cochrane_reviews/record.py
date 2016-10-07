# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Json


class Record(base.Record):
    table = 'cochrane_reviews'

    # Fields

    id = Text(primary_key=True)
    study_id = Text()
    file_name = Text()
    study_type = Text()
    doi_id = Text()
    robs = Json()
    refs = Json()
