# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from scrapy import Field
from six import add_metaclass
from abc import ABCMeta, abstractmethod
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from . import helpers


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

    def __init__(self, true_value=None):
        self.__true_value = true_value

    def parse(self, value):
        if self.__true_value is not None:
            value = (value.lower() == self.__true_value.lower())
        return value


class Date(Base):

    # Public

    type = sa.Date

    def __init__(self, format):
        self.__format = format

    def parse(self, value):
        return helpers.parse_date(value, format=self.__format)


class Datetime(Base):

    # Public

    type = sa.DateTime(timezone=True)

    def __init__(self, format=None):
        self.__format = format

    def parse(self, value):
        if self.__format is not None:
            value = helpers.parse_datetime(value, format=self.__format)
        return value


class Json(Base):

    # Public

    type = JSONB


class Array(Base):

    # Public

    def __init__(self, field=None):
        if field is None:
            field = Text()
        self.__field = field
        self.__type = ARRAY(field.type)

    @property
    def type(self):
        return self.__type

    def parse(self, value):
        result = []
        for item in value:
            result.append(self.__field.parse(item))
        return result
