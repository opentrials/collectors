# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
from .. import base
from .record import Record


# Module API

def parse_record(res):

    # Init data
    data = {}

    # Parse rawdata
    gpath = 'h1'
    kpath = 'p.eyebrowbold'
    vpath = 'p.eyebrowbold+*'
    rawdata = _parse_data(res, gpath, kpath, vpath)
    for group, key, value in rawdata:

        # General

        if key == 'compound':
            value = value.split(',')

        # Recruitment

        if key == 'locations':
            value = value.split(',')

        # Collect plain values
        data[key] = value

    # Extract results URL
    selector = '#results div a::attr(href)'
    value = res.css(selector).extract_first()
    if value:
        url = urlparse.urljoin(res.url, value)
        data['download_the_clinical_trial_summary'] = url
    else:
        try:
            del data['download_the_clinical_trial_summary']
        except KeyError:
            pass

    # Create record
    record = Record.create(res.url, data)

    return record


# Internal

def _parse_data(sel, gpath, kpath, vpath):
    data = []
    group = None
    name = None
    value = None
    for sel in sel.css('%s, %s, %s' % (gpath, kpath, vpath)):
        text = _parse_text(sel)
        if sel.css(gpath):
            group = text
        elif sel.css(kpath):
            name = base.helpers.slugify(text)
        else:
            value = text
            if name and value:
                data.append((group, name, value))
            name = None
            value = None
    return data


def _parse_text(sel):
    text = ''
    texts = sel.xpath('.//text()').extract()
    if texts:
        text = ' '.join(texts).strip()
    return text
