# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy
import logging
import sqlalchemy as sa
from six import add_metaclass
from datetime import datetime
from abc import ABCMeta, abstractmethod

logger = logging.getLogger(__name__)


# Module API

@add_metaclass(ABCMeta)
class Item(scrapy.Item):

    # Public

    @classmethod
    def create(cls, source, **kwargs):
        self = cls(**kwargs)
        timestamp = datetime.utcnow()
        self.fields['meta_source'] = scrapy.Field()
        self.fields['meta_created'] = scrapy.Field(
                type=sa.DateTime(timezone=True))
        self.fields['meta_updated'] = scrapy.Field(
                type=sa.DateTime(timezone=True))
        self.add_data({'meta_source': source})
        self.add_data({'meta_created': timestamp})
        self.add_data({'meta_updated': timestamp})
        return self

    def __repr__(self):
        template = '<%s: %s [%s]>'
        text = template % (
                self.table.upper(),
                self.get(self.primary_key),
                self.get(self.updated_key))
        return text

    @property
    @abstractmethod
    def table(self):
        """Source name.
        """
        pass  # pragma: no cover

    @property
    @abstractmethod
    def primary_key(self):
        """Item primary key.
        """
        pass  # pragma: no cover

    @property
    @abstractmethod
    def updated_key(self):
        """Item updated key.
        """
        pass  # pragma: no cover

    @property
    def types(self):
        """Item types.
        """
        types = {}
        for key, field in self.fields.items():
            type = field.get('type', sa.Text())
            types[key] = type
        return types

    def add_data(self, data):
        """Add data to item.
        """
        for key, value in data.items():
            field = self.fields.get(key)
            if field is None:
                logger.info('Undefined field: %s: %s=%s' % (self, key, value))
                continue
            if value is None:
                continue
            self[key] = value
