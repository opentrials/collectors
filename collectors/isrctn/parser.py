# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from .record import IsrctnRecord


# Module API

def parse(res):

    # Init data
    data = {}

    # General

    key = 'isrctn_id'
    path = '.ComplexTitle_primary::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'doi_isrctn_id'
    path = '.ComplexTitle_secondary::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'title'
    path = '//h1/text()'
    value = res.xpath(path).extract_first()
    data[key] = value

    kpath = '.Meta_name'
    vpath = '.Meta_name+.Meta_value'
    subdata = _parse_dict(res, kpath, vpath)
    data.update(subdata)

    tag = 'h3'
    text = 'Plain English Summary'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    section = _select_parent(res, tag, text)
    subdata = _parse_dict(section, kpath, vpath)
    data.update(subdata)

    # Contact information

    key = 'contacts'
    tag = 'h2'
    text = 'Contact information'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    first = 'type'
    section = _select_parent(res, tag, text)
    value = _parse_list(section, kpath, vpath, first)
    data.update({key: value})

    # Additional identifiers

    tag = 'h2'
    text = 'Additional identifiers'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    section = _select_parent(res, tag, text)
    subdata = _parse_dict(section, kpath, vpath)
    data.update(subdata)

    # Study information

    tag = 'h2'
    text = 'Study information'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    section = _select_parent(res, tag, text)
    subdata = _parse_dict(section, kpath, vpath)
    data.update(subdata)

    # Eligibility

    tag = 'h2'
    text = 'Eligibility'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    section = _select_parent(res, tag, text)
    subdata = _parse_dict(section, kpath, vpath)
    data.update(subdata)

    # Locations

    tag = 'h2'
    text = 'Locations'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    section = _select_parent(res, tag, text)
    subdata = _parse_dict(section, kpath, vpath)
    data.update(subdata)

    # Sponsor information

    key = 'sponsors'
    tag = 'h2'
    text = 'Sponsor information'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    first = 'organisation'
    section = _select_parent(res, tag, text)
    value = _parse_list(section, kpath, vpath, first)
    data.update({key: value})

    # Funders

    # TODO: fix logic
    key = 'funders'
    tag = 'h2'
    text = 'Funders'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    first = 'funder_type'
    section = _select_parent(res, tag, text)
    value = _parse_list(section, kpath, vpath, first)
    data.update({key: value})

    # Results and publications

    tag = 'h2'
    text = 'Results and Publications'
    kpath = '.Info_section_title'
    vpath = '.Info_section_title+p'
    section = _select_parent(res, tag, text)
    subdata = _parse_dict(section, kpath, vpath)
    data.update(subdata)

    # Create record
    record = IsrctnRecord.create(res.url, data)

    return record


# Internal

def _select_parent(sel, tag, text):
    return sel.xpath('//%s[contains(.,"%s")]/..' % (tag, text))


def _parse_dict(sel, kpath, vpath):
    """parse data from title-paragraph like html.
    """
    data = {}
    key = None
    value = None
    for sel in sel.css('%s, %s' % (kpath, vpath)):
        if sel.css(kpath):
            key = None
            value = None
            texts = sel.xpath('.//text()').extract()
            if texts:
                key = base.helpers.slugify(' '.join(texts).strip())
        else:
            if key is not None:
                value = None
                texts = sel.xpath('.//text()').extract()
                if texts:
                    value = ' '.join(texts).strip()
        if key and value:
            data[key] = value
    return data


def _parse_list(sel, kpath, vpath, first):
    """parse data from title-paragraph like html.
    """
    data = []
    item = {}
    key = None
    value = None
    for sel in sel.css('%s, %s' % (kpath, vpath)):
        if sel.css(kpath):
            key = None
            value = None
            texts = sel.xpath('.//text()').extract()
            if texts:
                key = base.helpers.slugify(' '.join(texts).strip())
        else:
            if key is not None:
                value = None
                texts = sel.xpath('.//text()').extract()
                if texts:
                    value = ' '.join(texts).strip()
        if key and value:
            item[key] = value
        if key == first and value is None and item:
            data.append(item)
            item = {}
    if item:
        data.append(item)
    return data
