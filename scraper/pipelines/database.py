# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import dataset
import logging

from .. import settings
logger = logging.getLogger(__name__)


# Module API

class Database(object):

    # Public

    def open_spider(self, spider):
        self.db = dataset.connect(settings.DATABASE_URL)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        table = self.db.get_table(
                spider.name,
                primary_id=item.primary_key,
                primary_type='String')
        if table.find_one(**{item.primary_key: item[item.primary_key]}):
            del item['meta_created']
        table.upsert(item, [item.primary_key], types=item.types)
        logger.info('Saved item: %s', item)
        return item
