# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from .record import TakedaRecord


# Module API

def extract_record(res):

    # Init data
    data = {}

    # Extract rawdata
    gpath = 'h1'
    kpath = 'p.eyebrowbold'
    vpath = 'p.eyebrowbold+*'
    rawdata = _extract_data(res, gpath, kpath, vpath)
    for group, key, value in rawdata:

        # General

        if key == 'takeda_trial_id':
            value = 'TAKEDA%s' % value

        if key == 'compound':
            value = value.split(',')

        # Recruitment

        if key == 'locations':
            value = value.split(',')

        # Collect plain values
        data[key] = value

    # Create record
    record = TakedaRecord.create(res.url, data)

    return record


# Internal

def _extract_data(sel, gpath, kpath, vpath):
    data = []
    group = None
    name = None
    value = None
    for sel in sel.css('%s, %s, %s' % (gpath, kpath, vpath)):
        text = _extract_text(sel)
        if sel.css(gpath):
            group = text
        elif sel.css(kpath):
            name = base._slugify(text)
        else:
            value = text
            if name and value:
                data.append((group, name, value))
            name = None
            value = None
    return data


def _extract_text(sel):
    text = ''
    texts = sel.xpath('.//text()').extract()
    if texts:
        text = ' '.join(texts).strip()
    return text
