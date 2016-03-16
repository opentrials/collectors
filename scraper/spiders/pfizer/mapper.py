# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from .item import PfizerItem


# Module API

class PfizerMapper(base.Mapper):

    # Public

    def map_response(self, res):

        # Init data
        data = {}

        # Description

        key = 'study_type'
        path = '.field-name-field-study-type .field-item::text'
        value = res.css(path).extract_first()
        data[key] = value

        key = 'organization_id'
        path = '.field-name-field-organization-id .field-item::text'
        value = res.css(path).extract_first()
        data[key] = value

        key = 'nct_id'
        path = '.field-name-field-clinical-trial-id .field-item::text'
        value = res.css(path).extract_first()
        data[key] = value

        key = 'status'
        path = '//label[text() = "Status"]/../text()'
        value = ''.join(res.xpath(path).extract()).strip()
        data[key] = value

        key = 'study_start_date'
        path = '.field-name-field-study-start-date .field-item span::text'
        value = res.css(path).extract_first()
        data[key] = value

        key = 'study_end_date'
        path = '.field-name-field-study-end-date .field-item span::text'
        value = res.css(path).extract_first()
        data[key] = value

        # Eligibility

        key = 'eligibility_criteria'
        path = '.field-name-field-criteria .field-item *::text'
        value = ''.join(res.css(path).extract())
        data[key] = value

        key = 'gender'
        path = '.field-name-field-gender .field-item::text'
        value = res.css(path).extract_first()
        data[key] = value

        key = 'age_range'
        path = '//label[text() = "Age Range:"]/../text()'
        value = ''.join(res.xpath(path).extract()).strip()
        data[key] = value

        key = 'healthy_volunteers_allowed'
        path = '.field-name-field-healthy-volunteers-allowed .field-item::text'
        value = res.css(path).extract_first()
        data[key] = value

        # Create item
        item = PfizerItem.create(res.url, data)

        return item
