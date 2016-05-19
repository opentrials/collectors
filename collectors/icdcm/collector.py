# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import logging
import zipfile
import requests
from scrapy.http import TextResponse
from .. import base
from .record import Record
logger = logging.getLogger(__name__)


# Module API

def collect(conf, conn):
    """Collect ICD-XX-CM conditions.
    """

    # For more information see:
    # https://www.cms.gov/Medicare/Coding/ICD10/2016-ICD-10-CM-and-GEMs.html
    URL = 'https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2016-CM-Code-Tables-and-Index.zip'
    FILE = 'Tabular.xml'
    VERSION = 'ICD-10-CM'
    LAST_UPDATED = '2015-10-01'

    # Prepare xml
    zip = requests.get(URL).content
    xml = zipfile.ZipFile(io.BytesIO(zip)).open(FILE).read()
    res = TextResponse(url=URL, body=xml, encoding='utf-8')

    count = 0
    for diag in res.xpath('//diag'):

        # We need only leafs
        childs = diag.xpath('./diag')
        if not childs:
            continue

        # Get data
        data = {}
        data['name'] = diag.xpath('./name/text()').extract_first()
        data['desc'] = diag.xpath('./desc/text()').extract_first()
        data['terms'] = diag.xpath('.//note/text()').extract()
        data['version'] = VERSION
        data['last_updated'] = LAST_UPDATED

        # Create record
        record = Record.create(URL, data)

        # Write record
        base.writers.write_record(conn, record)

        # Log info
        count += 1
        if not count % 100:
            logger.info('Collected %s "%s" conditions', count, record.table)
