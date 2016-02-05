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
        return {key: base.utils.parse_date(value, format='%Y-%m-%d')}

    # Summary

    date_on_which_this_record_was_first_entered = map_date

    # F. Population of Trial Subjects

    def subject_number_of_subjects_for_this_age_range(self, key, value):
        return {}
