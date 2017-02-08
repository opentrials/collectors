# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import zipfile
import logging
import requests
import tempfile
import contextlib
from datetime import datetime
from .parser import parse_record
from .. import base
logger = logging.getLogger(__name__)

# Module API


def collect(conf, conn, date_from=None, date_to=None):
    base.helpers.start(conf, 'nct', {})
    if not date_to:
        date_to = datetime.strftime(datetime.now(), '%Y-%m-%d')

    base_url = 'https://clinicaltrials.gov/search'
    query = {
        'resultsxml': True,
        'rcv_s': datetime.strptime(date_from, '%Y-%m-%d').strftime('%m/%d/%Y'),
        'rcv_e': datetime.strptime(date_to, '%Y-%m-%d').strftime('%m/%d/%Y'),
    }

    with tempfile.TemporaryFile() as fp:
        _download_to_file(base_url, fp, query)
        file_count = 0
        for identifier, record_fp in _iter_nct_dump_files(fp):
            try:
                rec = parse_record(record_fp)
                query = {'nct_id': rec['nct_id']}
                if rec.table in conn['warehouse'].tables:
                    existing = conn['warehouse'][rec.table].find_one(**query)
                    if existing:
                        rec['nct_id'] = existing['nct_id']
                rec.write(conf, conn)
                file_count += 1
            except Exception:
                base.config.SENTRY.captureException(extra={
                    'identifier': identifier,
                })
        logger.info('Collected %s NCT records', file_count)

    base.helpers.stop(conf, 'nct', {'collected': file_count})


def _download_to_file(url, fp, params):
    CHUNK_SIZE = 1024 * 1024  # 1 MB
    bytes_to_mb = lambda value: value / 1048576.0
    with contextlib.closing(requests.get(url, params=params, stream=True)) as response:
        completed_bytes = 0
        chunk_count = 0
        for block in response.iter_content(CHUNK_SIZE):
            fp.write(block)
            completed_bytes += len(block)
            chunk_count += 1
            if chunk_count % 1000 == 0:
                logger.debug('Downloaded %.2f MB', bytes_to_mb(completed_bytes))
    fp.seek(0)


def _iter_nct_dump_files(fp):
    with zipfile.ZipFile(fp) as archive:
        for filename in archive.namelist():
            identifier = filename.split('.')[0]
            with archive.open(filename, 'rU') as rec_file:
                yield identifier, rec_file
