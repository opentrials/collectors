# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import json
import logging
import zipfile
import requests
from .. import base
from .record import Record
logger = logging.getLogger(__name__)


# Module API

# For more information see:
# https://open.fda.gov/api/reference/
URL = 'http://download.open.fda.gov/drug/label/{file}.zip'
FILES = [
    'drug-label-0001-of-0005.json',
    'drug-label-0002-of-0005.json',
    'drug-label-0003-of-0005.json',
    'drug-label-0004-of-0005.json',
    'drug-label-0005-of-0005.json',
]


def collect(conf, conn):

    # Prepare pipiline
    # TODO: refactor pipelines to use without hacks
    spider = type(b'Spider', (object,), {'conn': conn})
    pipeline = base.pipelines.Warehouse()
    pipeline.open_spider(spider)

    errors = 0
    success = 0
    for file in FILES:

        # Get response
        url = URL.format(file=file)
        zip = requests.get(url).content
        res = json.load(zipfile.ZipFile(io.BytesIO(zip)).open(file))

        for item in res['results']:

            try:

                # Skip if no NDC code
                if 'product_ndc' not in item['openfda']:
                    continue

                # Get data
                data = {}
                data['product_ndc'] = item['openfda']['product_ndc'][0]
                data['product_type'] = item['openfda']['product_type'][0]
                data['generic_name'] = item['openfda']['generic_name'][0]
                data['brand_name'] = item['openfda']['brand_name'][0]
                data['last_updated'] = res['meta']['last_updated']

                # Create record
                record = Record.create(url, data)

                # Write record
                pipeline.process_item(record, spider)

                # Log info
                success += 1
                if not success % 100:
                    logger.info('Collected %s "%s" interventions',
                        success, record.table)

            except Exception as exception:

                # Log warning
                errors += 1
                logger.warning('Collecting error: %s', repr(exception))
