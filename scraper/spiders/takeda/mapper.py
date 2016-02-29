# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .item import Item


# Module API

class Mapper(base.Mapper):

    # Public

    def map_response(self, res):

        # Init data
        data = {}

        # Extract rawdata
        gpath = 'h1'
        kpath = 'p.eyebrowbold'
        vpath = 'p.eyebrowbold+*'
        rawdata = utils.extract_data(res, gpath, kpath, vpath)
        for group, key, value in rawdata:

            # General

            if key == 'compound':
                value = value.split(',')

            # Recruitment

            if key == 'locations':
                value = value.split(',')

            # Collect plain values
            data[key] = value

        # Create item
        item = Item.create(res.url, data)

        return item
