# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from .. import base
from . import utils
from .item import GskItem


# Module API

class GskMapper(base.Mapper):

    # Public

    remove = [
        'explanation',
    ]

    def map_response(self, res):  # noqa

        # Init data
        data = {}

        # Extract rawdata
        kpath = 'td.rowlabel'
        vpath = 'td.rowlabel+td'
        rawdata = utils.extract_data(res, kpath, vpath)
        for key, value in rawdata:

            # Protocol summary

            if key == 'secondary_ids':
                newvalue = []
                for element in re.split(r'\t+', value):
                    newvalue.append(element.strip())
                value = newvalue

            if key == 'oversight_authority':
                newvalue = []
                for element in re.split(r'\t+', value):
                    newvalue.append(element.strip())
                value = newvalue

            if key == 'primary_outcomes':
                newvalue = []
                for element in re.split(r'\t+', value):
                    elementdata = []
                    for subelement in element.splitlines():
                        subelement = subelement.strip()
                        if subelement:
                            elementdata.append(subelement)
                    newvalue.append(elementdata)
                value = newvalue

            if key == 'secondary_outcomes':
                newvalue = []
                for element in re.split(r'\t+', value):
                    elementdata = []
                    for subelement in element.splitlines():
                        subelement = subelement.strip()
                        if subelement:
                            elementdata.append(subelement)
                    newvalue.append(elementdata)
                value = newvalue

            if key == 'arms':
                newvalue = []
                for element in re.split(r'\t+', value):
                    elementdata = []
                    for subelement in element.splitlines():
                        subelement = subelement.strip()
                        if subelement:
                            elementdata.append(subelement)
                    newvalue.append(elementdata)
                value = newvalue

            if key == 'interventions':
                newvalue = []
                for element in re.split(r'\t+', value):
                    elementdata = []
                    for subelement in element.splitlines():
                        subelement = subelement.strip()
                        if subelement:
                            elementdata.append(subelement)
                    newvalue.append(elementdata)
                value = newvalue

            if key == 'conditions':
                newvalue = []
                for element in re.split(r'\t+', value):
                    newvalue.append(element.strip())
                value = newvalue

            if key == 'keywords':
                newvalue = []
                for element in re.split(r'\t+', value):
                    newvalue.append(element.strip())
                value = newvalue

            # Collect plain values
            data[key] = value

        # Date information
        nodes = res.css('#ps tr.header td')
        try:
            data['first_received'] = nodes[0].xpath('text()').extract_first()
            data['last_updated'] = nodes[1].xpath('text()').extract_first()
        except Exception:
            pass

        # Remove data
        for key in self.remove:
            if key in data:
                del data[key]

        # Remove data
        for key in self.remove:
            if key in data:
                del data[key]

        # Create item
        item = GskItem.create(res.url, data)

        return item
