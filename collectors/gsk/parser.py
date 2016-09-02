# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import re
from .. import base
from .record import Record


# Module API

def parse_record(res):
    fields_to_remove = [
        'explanation',
    ]

    # Init data
    data = {}

    # Parse rawdata
    kpath = 'td.rowlabel'
    vpath = 'td.rowlabel+td'
    rawdata = _parse_data(res, kpath, vpath)
    for key, value in rawdata:

        # General

        if key == 'study_id':
            value = 'GSK%s' % value

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

    # Results URL
    urls = res.css('#rs td a::attr(href)').extract()
    if urls:
        assert len(urls) == 1, 'Multiple URLs found on %s' % res.url
        data['results_url'] = urlparse.urljoin(res.url, urls[0])

    # Remove data
    for key in fields_to_remove:
        if key in data:
            del data[key]

    # Create record
    record = Record.create(res.url, data)

    return record


# Internal

def _parse_data(sel, kpath, vpath):
    data = []
    name = None
    value = None
    for sel in sel.css('%s, %s' % (kpath, vpath)):
        text = _parse_text(sel)
        if sel.css(kpath):
            name = base.helpers.slugify(text)
        else:
            value = text
            if name and value:
                data.append((name, value))
            name = None
            value = None
    return data


def _parse_text(sel):
    text = ''
    texts = sel.xpath('.//text()').extract()
    if texts:
        text = ' '.join(texts).strip()
    return text
