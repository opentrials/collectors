# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .item import Item


# Module API

class Mapper(base.Mapper):

    # Public

    merge = [
        'secondary_id',
        'intervention_code',
        'primary_outcome',
        'secondary_outcome',
        'timepoint',
        'recruitment_postcodes',
        'recruitment_hospital',
        'funding_source_category',
        'secondary_sponsor_category',
        'stateprovince',
        'ethics_approval_number',
        'ethics_committee_name',
        'ethics_committee_country',
        'ethics_committee_address',
        'approval_date',
        'name',
        'country',
        'address',
    ]

    remove = [
        'timepoints',
        'stateprovinces',
        'primary_sponsor_type',
        'funding_source_categorys',
        'secondary_sponsor_categorys',
        'names',
        'addresss',
        'countrys',
        'name',
        'address',
        'country',
        'phone',
        'fax',
        'email',
    ]

    def map_response(self, res):

        # Init data
        data = {}

        # Extract all data
        kpath = '.review-element-name'
        vpath = '.review-element-content'
        subdata = utils.extract_dict(res, kpath, vpath)
        data.update(subdata)

        # Merge data
        subdata = {}
        for key in self.merge:
            number = 0
            mulkey = key+'s'
            subdata[mulkey] = []
            while True:
                number += 1
                numkey = '_'.join([key, str(number)])
                if numkey not in data:
                    break
                subdata[mulkey].append(data.pop(numkey))
        data.update(subdata)

        # Remove data
        for key in self.remove:
            if key in data:
                del data[key]

        # Create item
        item = Item.create(res.url, data)

        return item
