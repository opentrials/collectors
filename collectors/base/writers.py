# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)


# Module API

def write_record(conn, record):
    """Write record to warehouse.

    Args:
        conn (dict): connections dictionary
        record (dict): record dictionary

    """
    table = conn['warehouse'].get_table(
            record.table,
            primary_id=record.primary_key,
            primary_type='String')
    action = 'created'
    if table.find_one(**{record.primary_key: record[record.primary_key]}):
        action = 'updated'
        for key in record.skip_on_update:
            del record[key]
    try:
        table.upsert(
            record, [record.primary_key],
            ensure=record.ensure_fields, types=record.types)
    except Exception as exception:
        logger.exception('Saving error: %s: %s' % (record, repr(exception)))
    else:
        logger.debug('Record - %s: %s - %s fields', action, record, len(record))
