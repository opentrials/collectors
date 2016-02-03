# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

logger = logging.getLogger(__name__)


# Module API

class Mapper(object):

    # Public

    def map_data(self, data):
        mapdata = {}
        for key, value in data.items():
            submapper = getattr(self, key, None)
            if submapper is not None:
                try:
                    subdata = submapper(key, value)
                except Exception:
                    if value is not None:
                        message = 'Mapping error: %s=%s'
                        message = message % (key, value)
                        logger.info(message)
                    continue
            else:
                subdata = {key: value}
            mapdata.update(subdata)
        return mapdata
