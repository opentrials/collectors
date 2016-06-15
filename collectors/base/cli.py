# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import dataset
import logging
from importlib import import_module
from . import config
from . import helpers
logger = logging.getLogger(__name__)


# Module API

def cli(argv):

    try:

        # Prepare conf dict
        conf = helpers.get_variables(config, str.isupper)

        # Prepare conn dict
        conn = {}
        conn['warehouse'] = dataset.connect(config.WAREHOUSE_URL2)

        # Get and call collector
        collect = import_module('collectors.%s' % argv[1]).collect
        collect(conf, conn, *argv[2:])

    except Exception as exception:

        # Log exception and raise
        logger.exception('Unhandled exception: %s', exception)
        raise


if __name__ == '__main__':
    cli(sys.argv)
