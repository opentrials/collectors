# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base


# Module API

class Mapper(base.Mapper):

    # Helpers

    def map_integer(self, key, value):
        return {key: int(value)}

    def map_month(self, key, value):
        return {key: base.utils.parse_date(value, format='%B %Y')}

    def map_date(self, key, value):
        return {key: base.utils.parse_date(value, format='%B %d, %Y')}

    # General

    start_date = map_month
    completion_date_actual = map_month
    completion_date_anticipated = map_month
    primary_completion_date_actual = map_month
    primary_completion_date_anticipated = map_month
    number_of_arms = map_integer
    number_of_groups = map_integer
    enrollment_actual = map_integer
    enrollment_anticipated = map_integer
    verification_date = map_month
    lastchanged_date = map_date
    firstreceived_date = map_date
    firstreceived_results_date = map_date
