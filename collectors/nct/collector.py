# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import zipfile
import logging
import io
import requests
from datetime import datetime
from .parser import parse_record
from .. import base
logger = logging.getLogger(__name__)

# Module API


def collect(conf, conn, date_from=None, date_to=None):
    file_count = 0
    base.helpers.start(conf, 'nct', {})
    if not date_to:
        date_to = datetime.strftime(datetime.now(), '%Y-%m-%d')

    base_url = 'https://clinicaltrials.gov/search'
    query = {
        'resultsxml': True,
        'rcv_s': datetime.strptime(date_from, '%Y-%m-%d').strftime('%m/%d/%Y'),
        'rcv_e': datetime.strptime(date_to, '%Y-%m-%d').strftime('%m/%d/%Y'),
    }
    content = requests.get(base_url, params=query).content

    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        for filename in archive.namelist():
            try:
                with archive.open(filename, 'rU') as rec_file:
                    rec = parse_record(rec_file)
                    query = {'nct_id': rec['nct_id']}
                    if rec.table in conn['warehouse'].tables:
                        existing = conn['warehouse'][rec.table].find_one(**query)
                        if existing:
                            rec['nct_id'] = existing['nct_id']
                    rec.write(conf, conn)
                    file_count += 1

            except Exception as exception:
                logger.exception(repr(exception), exc_info=True)

    logger.info("Collected %s NCT records", file_count)
    base.helpers.stop(conf, 'nct', {'collected': file_count})
