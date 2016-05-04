# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from importlib import import_module
from collectors.euctr.spider import _make_start_urls


# Tests

def test_make_start_urls():
    result = _make_start_urls(
            'https://www.clinicaltrialsregister.eu/ctr-search/search',
            '2015-01-01', '2015-01-02')
    print(result)
    assert result
