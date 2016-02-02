# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


# Module API

class Mapper(object):

    # Public

    def map_data(self, data):
        mapdata = {}
        for key, value in data.items():
            subparser = getattr(self, key, None)
            if subparser is not None:
                subdata = subparser(key, value)
            else:
                subdata = {key: value}
            mapdata.update(subdata)
        return mapdata
