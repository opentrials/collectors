# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from scrapy import Field
from six import add_metaclass
from abc import ABCMeta, abstractmethod
from sqlalchemy.dialects.postgresql import ARRAY, JSON

from . import utils


@add_metaclass(ABCMeta)
class Base(Field):

    # Public

    def __repr__(self):
        return type(self).__name__

    @property
    @abstractmethod
    def type(self):
        pass  # pragma: no cover

    def parse(self, value):
        return value


class Text(Base):

    # Public

    type = sa.Text


class Integer(Base):

    # Public

    type = sa.Integer

    def parse(self, value):
        return int(value)


class Boolean(Base):

    # Public

    type = sa.Boolean

    def __init__(self, true_value):
        self.true_value = true_value

    def parse(self, value):
        return value == self.true_value


class Date(Base):

    # Public

    type = sa.Date

    def __init__(self, format):
        self.format = format

    def parse(self, value):
        return utils.parse_date(value, format=self.format)


class Datetime(Base):

    # Public

    def __init__(self, format=None):
        self.format = format

    type = sa.DateTime(timezone=True)

    def parse(self, value):
        if self.format is not None:
            value = utils.parse_datetime(value, format=self.format)
        return value


class Json(Base):

    # Public

    type = JSON


class Array(Base):

    # Public

    type = ARRAY(sa.Text)
