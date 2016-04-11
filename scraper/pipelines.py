# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import dataset
import logging

from . import settings
logger = logging.getLogger(__name__)


# Module API

class Database(object):

    # Public

    def open_spider(self, spider):
        self.db = dataset.connect(settings.WAREHOUSE_URL)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        table = self.db.get_table(
                item.table,
                primary_id=item.primary_key,
                primary_type='String')
        action = 'Created'
        if table.find_one(**{item.primary_key: item[item.primary_key]}):
            action = 'Updated'
            for key in item.skip_on_update:
                del item[key]
        try:
            table.upsert(
                item, [item.primary_key],
                ensure=item.ensure_fields, types=item.types)
        except Exception as exception:
            logger.warning('Saving error: %s: %s' % (item, repr(exception)))
        else:
            logger.debug('%s item: %s - %s fields', action, item, len(item))
        return item
