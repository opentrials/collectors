# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import OrderedDict
from .. import base
from .record import JprnRecord


# Module API

def parse_record(res):
    fields_to_remove = [
        'item',
    ]

    # Parse rawdata
    data = {}

    # Get meta
    subdata = _parse_table(res, key_index=0, value_index=2)
    data.update(subdata)

    # Process rawdata
    rawdata = _parse_table(res, key_index=0, value_index=1)
    prefix = ''
    for key, value in rawdata.items():

        # Interventions

        newkey = 'interventions'
        oldkey = 'interventionscontrol'
        data.setdefault(newkey, [])
        if key.startswith(oldkey):
            data[newkey].append(value)
            continue

        # Research contact person

        if key == 'name_of_lead_principal_investigator':
            prefix = 'research_'

        # Public contact

        if key == 'name_of_contact_person':
            prefix = 'public_'

        # Sponsor

        if key == 'name_of_primary_sponsor':
            prefix = ''

        # Collect plain values
        key = prefix + key
        data[key] = value

    # Remove data
    for key in fields_to_remove:
        if key in data:
            del data[key]

    # Create record
    record = JprnRecord.create(res.url, data)

    return record


# Internal

def _parse_table(res, key_index, value_index):
    """parse data from tabular structure.
    """
    data = OrderedDict()
    for sel in res.xpath('//tr'):
        columns = sel.xpath('td')
        if len(columns) == value_index+1:
            key = ''.join(columns[key_index].xpath('.//text()').extract())
            key = base.helpers.slugify(key.strip())
            value = ''.join(columns[value_index].xpath('.//text()').extract())
            value = value.strip()
            if key and value:
                data[key] = value
    return data
