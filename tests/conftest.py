# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest
import dataset
from collectors.base import config, helpers


# Fixtures

@pytest.fixture
def conf():
    return helpers.get_variables(config, str.isupper)


@pytest.fixture
def conn():
    warehouse = dataset.connect(config.TEST_WAREHOUSE_URL)
    for table in warehouse.tables:
        warehouse[table].delete()
    return {'warehouse': warehouse}
