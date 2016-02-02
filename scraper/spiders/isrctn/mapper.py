# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base


# Module API

class Mapper(base.Mapper):

    # Dates

    def date_applied(self, key, value):
        return {key: base.utils.parse_date(value, format='%d/%m/%Y')}

    date_assigned = date_applied
    last_edited = date_applied
    overall_trial_start_date = date_applied
    overall_trial_end_date = date_applied
    recruitment_start_date = date_applied
    recruitment_end_date = date_applied
    intention_to_publish_date = date_applied
