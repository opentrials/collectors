# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from importlib import import_module

from scraper.spiders.isrctn.utils import make_start_urls


def test_make_start_urls():
    result = make_start_urls('prefix', '2016-01-01', '2016-01-15')
    print(result)
    assert result
