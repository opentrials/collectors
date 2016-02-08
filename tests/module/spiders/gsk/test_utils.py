# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from importlib import import_module
module = import_module('scraper.spiders.gsk.utils')


def test_make_start_urls():
    result = module.make_start_urls(
            'http://www.gsk-clinicalstudyregister.com/search',
            '2015-01-01', '2015-01-31')
    print(result)
    assert result
