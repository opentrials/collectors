# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .item import JprnItem


# Module API

class JprnMapper(base.Mapper):

    # Public

    remove = [
        'item',
    ]

    def map(self, res):

        # Extract rawdata
        data = {}

        # Get meta
        subdata = utils.extract_table(res, key_index=0, value_index=2)
        data.update(subdata)

        # Process rawdata
        rawdata = utils.extract_table(res, key_index=0, value_index=1)
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
        for key in self.remove:
            if key in data:
                del data[key]

        # Create item
        item = JprnItem.create(res.url, data)

        return item
