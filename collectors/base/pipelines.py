# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import dataset
from . import config
from . import helpers


# Module API

class Warehouse(object):

    # Public

    def open_spider(self, spider):
        if spider.conf and spider.conn:
            self.__conf = spider.conf
            self.__conn = spider.conn
        else:
            # For runs trigered by scrapy CLI utility
            self.__conf = helpers.get_variables(config, str.isupper)
            self.__conn = {'warehouse': dataset.connect(config.WAREHOUSE_URL)}

    def process_item(self, record, spider):
        record.write(self.__conf, self.__conn)
        return record
