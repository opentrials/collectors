# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import dataset
import logging
from . import config
logger = logging.getLogger(__name__)


# Module API

class Warehouse(object):

    # Public

    def open_spider(self, spider):
        if spider.conn:
            self._warehouse = spider.conn['warehouse']
        else:
            # For runs trigered by scrapy cli utility
            self._warehouse = dataset.connect(config.WAREHOUSE_URL)

    def process_item(self, record, spider):
        table = self._warehouse.get_table(
                record.table,
                primary_id=record.primary_key,
                primary_type='String')
        action = 'created'
        if table.find_one(**{record.primary_key: record[record.primary_key]}):
            action = 'updated'
            for key in record.skip_on_update:
                del record[key]
        try:
            table.upsert(
                record, [record.primary_key],
                ensure=record.ensure_fields, types=record.types)
        except Exception as exception:
            logger.warning('Saving error: %s: %s' % (record, repr(exception)))
        else:
            logger.debug('Record - %s: %s - %s fields', action, record, len(record))
        return record
