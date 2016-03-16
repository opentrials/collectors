# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from six import add_metaclass
from abc import ABCMeta, abstractmethod


# Module API

@add_metaclass(ABCMeta)
class Mapper(object):

    # Public

    @abstractmethod
    def map(self, res):
        """Map response to item.

        Args:
            res (object): http response

        Returns:
            dict: item

        """
        pass  # pragma: no cover
