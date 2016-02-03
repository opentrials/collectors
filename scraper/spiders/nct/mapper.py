# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base


# Module API

class Mapper(base.Mapper):

    # Integers

    def map_integer(self, key, value):
        if value is not None:
            value = int(value)
        return {key: value}

    number_of_arms = map_integer
    number_of_groups = map_integer
    enrollment_actual = map_integer
    enrollment_anticipated = map_integer
