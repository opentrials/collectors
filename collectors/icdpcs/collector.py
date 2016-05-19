# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import logging
import zipfile
import requests
from .. import base
from .record import Record
logger = logging.getLogger(__name__)


# Module API

def collect(conf, conn):
    """Collect ICD-XX-PCS procedures.
    """

    # For more information see:
    # https://www.cms.gov/Medicare/Coding/ICD10/2016-ICD-10-PCS-and-GEMs.html
    URL = 'https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2016-PCS-Long-Abbrev-Titles.zip'
    FILE = 'icd10pcs_order_2016.txt'
    VERSION = 'ICD-10-PCS'
    LAST_UPDATED = '2015-10-01'

    # Prepare file
    zip = requests.get(URL).content
    file = zipfile.ZipFile(io.BytesIO(zip)).open(FILE)

    count = 0
    for line in file:

        # Prepare data
        # Format is described in instruction
        # stored in zip archive we download
        data = {}
        data['code'] = line[6:6+7].strip()
        data['is_header'] = line[14:14+1].strip()
        data['short_description'] = line[16:16+60].strip()
        data['long_description'] = line[77:].strip()
        data['version'] = VERSION
        data['last_updated'] = LAST_UPDATED

        # Create record
        record = Record.create(URL, data)

        # Write record
        base.writers.write_record(conn, record)

        # Log info
        count += 1
        if not count % 100:
            logger.info('Collected %s "%s" interventions', count, record.table)
