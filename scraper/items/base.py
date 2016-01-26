# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy
from six import add_metaclass
from abc import ABCMeta, abstractmethod


# Module API

@add_metaclass(ABCMeta)
class Base(scrapy.Item):

    # Public

    @abstractmethod
    def __repr__(self):
        pass  # pragma: no cover

    def add_data(self, key, value):
        if key in self.fields:
            self[key] = value
