# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base


class EpistemonikosItem(base.Record):

    citation = Text()
    title = Text()
    abstract = Text()
