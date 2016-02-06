# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from importlib import import_module
module = import_module('scraper.spiders.euctr.utils')


def test_make_start_urls():
    result = module.make_start_urls(
            'https://www.clinicaltrialsregister.eu/ctr-search/search',
            '2015-01-01', '2015-01-02')
    print(result)
    assert result


def test_make_pattetn():
    result = module.make_pattern('ctr-search/search')
    print(result)
    assert result
