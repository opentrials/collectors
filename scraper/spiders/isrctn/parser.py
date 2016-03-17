# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .item import IsrctnItem


# Module API

class IsrctnParser(base.Parser):

    # Public

    def parse(self, res):

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
        subdata = utils.extract_dict(res, kpath, vpath)
        data.update(subdata)

        tag = 'h3'
        text = 'Plain English Summary'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Contact information

        key = 'contacts'
        tag = 'h2'
        text = 'Contact information'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        first = 'type'
        section = utils.select_parent(res, tag, text)
        value = utils.extract_list(section, kpath, vpath, first)
        data.update({key: value})

        # Additional identifiers

        tag = 'h2'
        text = 'Additional identifiers'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Study information

        tag = 'h2'
        text = 'Study information'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Eligibility

        tag = 'h2'
        text = 'Eligibility'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Locations

        tag = 'h2'
        text = 'Locations'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Sponsor information

        key = 'sponsors'
        tag = 'h2'
        text = 'Sponsor information'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        first = 'organisation'
        section = utils.select_parent(res, tag, text)
        value = utils.extract_list(section, kpath, vpath, first)
        data.update({key: value})

        # Funders

        key = 'funders'
        tag = 'h2'
        text = 'Funders'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        first = 'funder_type'
        section = utils.select_parent(res, tag, text)
        value = utils.extract_list(section, kpath, vpath, first)
        data.update({key: value})

        # Results and publications

        tag = 'h2'
        text = 'Results and Publications'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Create item
        item = IsrctnItem.create(res.url, data)

        return item
