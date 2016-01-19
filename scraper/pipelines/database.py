# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import dataset
import logging

from .. import settings
logger = logging.getLogger(__name__)


class Database(object):

    # Public

    def open_spider(self, spider):
        self.db = dataset.connect(settings.DATABASE_URL)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        table = self.db.get_table(spider.name)
        table.insert(item)
        logger.info('Saved %s', item)
        return item
