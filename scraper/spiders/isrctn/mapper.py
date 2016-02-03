# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base


# Module API

class Mapper(base.Mapper):

    # Helpers

    def map_date(self, key, value):
        return {key: base.utils.parse_date(value, format='%d/%m/%Y')}

    # General

    date_applied = map_date
    date_assigned = map_date
    last_edited = map_date

    # Study information

    overall_trial_start_date = map_date
    overall_trial_end_date = map_date

    # Eligibility

    recruitment_start_date = map_date
    recruitment_end_date = map_date

    # Result and publications

    intention_to_publish_date = map_date
