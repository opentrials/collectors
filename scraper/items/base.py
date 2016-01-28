# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from six import add_metaclass
from datetime import datetime
from scrapy import Item, Field
from abc import ABCMeta, abstractmethod


# Module API

@add_metaclass(ABCMeta)
class Base(Item):

    # Public

    @classmethod
    def create(cls, source, *args, **kwargs):
        self = cls(*args, **kwargs)
        timestamp = datetime.utcnow()
        self.fields['meta_source'] = Field()
        self.fields['meta_created'] = Field(type=sa.DateTime(timezone=True))
        self.fields['meta_updated'] = Field(type=sa.DateTime(timezone=True))
        self.add_data('meta_source', source)
        self.add_data('meta_created', timestamp)
        self.add_data('meta_updated', timestamp)
        return self

    def __repr__(self):
        template = '<%s: %s [%s]>'
        text = template % (
                type(self).__name__.upper(),
                self.get(self.primary_key),
                self.get(self.updated_key))
        return text

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

    def add_data(self, key, value):
        """Save field value.
        """
        field = self.fields.get(key)
        if field is not None:
            parser = field.get('parser')
            if parser is not None:
                value = parser(value)
            self[key] = value
