# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import ijson
import shutil
import logging
import zipfile
import tempfile
import requests
from .record import Record
logger = logging.getLogger(__name__)


# Module API

def collect(conf, conn):
    """Collect FDA Drug Labels.
    """

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

    # Create temp directory
    dirpath = tempfile.mkdtemp()

    errors = 0
    success = 0
    for file in FILES:

        # Download json
        url = URL.format(file=file)
        arch = zipfile.ZipFile(io.BytesIO(requests.get(url).content))
        path = arch.extract(file, dirpath)
        file = io.open(path, encoding='utf-8')

        # Get last updated
        last_updated = list(ijson.items(file, 'meta.last_updated'))[0]

        # Get items iterator
        file.seek(0)
        items = ijson.items(file, 'results.item')

        for item in items:

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
                data['last_updated'] = last_updated

                # Create record
                record = Record.create(url, data)

                # Write record
                record.write(conn)

                # Log info
                success += 1
                if not success % 100:
                    logger.info('Collected %s "%s" interventions',
                        success, record.table)

            except Exception as exception:

                # Log exception
                errors += 1
                logger.exception('Collecting error: %s', repr(exception))

    # Remove temp directory
    shutil.rmtree(dirpath)
