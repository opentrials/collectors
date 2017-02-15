# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import datetime
import pytest
import collectors.base.fields as fields


class TestFields(object):
    def test_date_accepts_single_format(self):
        date = fields.Date('%Y-%m')

        assert date.parse('2017-01') == datetime.date(2017, 1, 1)

    def test_date_accepts_multiple_formats(self):
        date = fields.Date(['%Y-%m', '%Y-%m-%d'])

        assert date.parse('2017-01') == datetime.date(2017, 1, 1)
        assert date.parse('2017-01-01') == datetime.date(2017, 1, 1)

    def test_date_raises_if_date_is_in_wrong_format(self):
        date = fields.Date('%Y-%m')
        with pytest.raises(ValueError):
            date.parse('2017-01-01')
