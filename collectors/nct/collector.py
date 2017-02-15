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
from .parser import parse_record
from .. import base
logger = logging.getLogger(__name__)

# Module API


def collect(conf, conn, nct_xml_dump_url):
    '''
    Downloads and parse data from NCT's XML dump. Considering you want the data
    from 2017-01-01 until 2017-02-01, the XML dump can be downloaded from:

    https://clinicaltrials.gov/search?resultsxml=True&rcv_s=01/01/2017&rcv_e=01/02/2017
    '''
    base.helpers.start(conf, 'nct', {'url': nct_xml_dump_url})

    with tempfile.TemporaryFile() as fp:
        _download_to_file(nct_xml_dump_url, fp)
        file_count = 0
        for identifier, record_fp in _iter_nct_dump_files(fp):
            base.config.SENTRY.extra_context({
                'url': nct_xml_dump_url,
                'identifier': identifier,
            })
            rec = parse_record(record_fp)
            query = {'nct_id': rec['nct_id']}
            if rec.table in conn['warehouse'].tables:
                existing = conn['warehouse'][rec.table].find_one(**query)
                if existing:
                    rec['nct_id'] = existing['nct_id']
            rec.write(conf, conn)
            file_count += 1
        logger.info('Collected %s NCT records', file_count)

    base.helpers.stop(conf, 'nct', {
        'url': nct_xml_dump_url,
        'collected': file_count,
    })


def _download_to_file(url, fp):
    CHUNK_SIZE = 1024 * 1024  # 1 MB
    bytes_to_mb = lambda value: value / 1048576.0
    with contextlib.closing(requests.get(url, stream=True)) as response:
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
