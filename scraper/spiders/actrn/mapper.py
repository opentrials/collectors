# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from .. import base
from . import utils
from .item import ActrnItem


# Module API

class ActrnMapper(base.Mapper):

    # Public

    remove = [
        'country',
        'stateprovince',
        'recruitment_postcodes',
        'recruitment_hospital',
    ]

    def map(self, res):  # noqa

        # Init data
        data = {}

        # Extract rawdata
        gpath = '.review-element-header, .health-header'
        kpath = '.review-element-name'
        vpath = '.review-element-content'
        rawdata = utils.extract_data(res, gpath, kpath, vpath)
        for group, key, value in rawdata:

            # Parse key
            index = None
            match = re.match(r'(.*?)(?:_(\d+))?_\d+_\d+', key)
            if match:
                key = match.group(1)
                index = match.group(2)
                if index is not None:
                    index = int(index) - 1

            # Titles & IDs

            newkey = 'secondary_ids'
            oldkey = 'secondary_id'
            data.setdefault(newkey, [])
            if key == oldkey:
                data[newkey].append(value)
                continue

            # Intervention/exposure

            newkey = 'intervention_codes'
            oldkey = 'intervention_code'
            data.setdefault(newkey, [])
            if key == oldkey:
                data[newkey].append(value)
                continue

            # Outcomes

            newkey = 'primary_outcomes'
            oldkey = 'primary_outcome'
            data.setdefault(newkey, [])
            if key == oldkey:
                outcome_key = newkey
                outcome_data = {'outcome': value}
                continue

            newkey = 'secondary_outcomes'
            oldkey = 'secondary_outcome'
            data.setdefault(newkey, [])
            if key == oldkey:
                outcome_key = newkey
                outcome_data = {'outcome': value}
                continue

            oldkey = 'timepoint'
            if key == oldkey:
                outcome_data['timepoint'] = value
                data[outcome_key].append(outcome_data)
                continue

            # Funding & Sponsors

            newkey = 'primary_sponsor'
            oldgroup = 'Funding & Sponsors'
            data.setdefault(newkey, {})
            if group == oldgroup:
                if index is None:
                    data[newkey][key] = value
                    continue

            newkey = 'sponsors'
            oldgroup = 'Funding & Sponsors'
            data.setdefault(newkey, [])
            if group == oldgroup:
                while len(data[newkey]) <= index:
                    data[newkey].append({})
                data[newkey][index][key] = value
                continue

            # Ethics approval

            newkey = 'ethics_application_status'
            if key == newkey:
                data[newkey] = value
                continue

            newkey = 'ethics_applications'
            oldgroup = 'Ethics approval'
            data.setdefault(newkey, [])
            if group == oldgroup:
                while len(data[newkey]) <= index:
                    data[newkey].append({})
                data[newkey][index][key] = value
                continue

            # Summary

            newkey = 'attachments'
            oldkey = 'attachments'
            data.setdefault(newkey, [])
            if key == oldkey:
                data[newkey].append(value)
                continue

            # Contacts

            newkey = 'principal_investigator'
            oldgroup = 'Principal investigator'
            data.setdefault(newkey, {})
            if group == oldgroup:
                data[newkey][key] = value
                continue

            newkey = 'public_queries'
            oldgroup = 'Contact person for public queries'
            data.setdefault(newkey, {})
            if group == oldgroup:
                data[newkey][key] = value
                continue

            newkey = 'scientific_queries'
            oldgroup = 'Contact person for scientific queries'
            data.setdefault(newkey, {})
            if group == oldgroup:
                data[newkey][key] = value
                continue

            # Collect plain values
            data[key] = value

        # Health condition

        key = 'health_conditions_or_problems_studied'
        path = '.review-element-content.health'
        value = res.css(path).xpath('span[1]/text()').extract_first()
        data[key] = value

        key = 'condition_category'
        path = '.review-element-condition'
        value = res.css(path).xpath('span[1]/text()').extract_first()
        data[key] = value

        key = 'condition_code'
        path = '.review-element-condition-right'
        value = res.css(path).xpath('span[1]/text()').extract_first()
        data[key] = value

        # Remove data
        for key in self.remove:
            if key in data:
                del data[key]

        # Create item
        item = ActrnItem.create(res.url, data)

        return item
