# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from .record import IctrpRecord
logger = logging.getLogger(__name__)


# Module API

def parse_record(res):

    # Init data
    data = {}

    # Main

    key = 'register'
    path = '#DataList3_ctl01_DescriptionLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'last_refreshed_on'
    path = '#DataList3_ctl01_Last_updatedLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'main_id'
    path = '#DataList3_ctl01_TrialIDLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'date_of_registration'
    path = '#DataList3_ctl01_Date_registrationLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'primary_sponsor'
    path = '#DataList3_ctl01_Primary_sponsorLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'public_title'
    path = '#DataList3_ctl01_Public_titleLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'scientific_title'
    path = '#DataList3_ctl01_Scientific_titleLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'date_of_first_enrollment'
    path = '#DataList3_ctl01_Date_enrollementLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'target_sample_size'
    path = '#DataList3_ctl01_Target_sizeLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'recruitment_status'
    path = '#DataList3_ctl01_Recruitment_statusLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'url'
    path = '#DataList3_ctl01_HyperLink12::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'study_type'
    path = '#DataList3_ctl01_Study_typeLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'study_design'
    path = '#DataList3_ctl01_Study_designLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'study_phase'
    path = '#DataList3_ctl01_PhaseLabel::text'
    value = res.css(path).extract_first()
    data[key] = value

    # Additional

    key = 'countries_of_recruitment'
    path = '//*[re:test(@id, "DataList2_ctl\d+_Country_Label")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'contacts'
    path_first_name = '#DataList4_ctl%s_FirstnameLabel::text'
    path_last_name = '#DataList4_ctl%s_LastnameLabel::text'
    path_address = '#DataList4_ctl%s_AddressLabel::text'
    path_telephone = '#DataList4_ctl%s_TelephoneLabel::text'
    path_email = '#DataList4_ctl%s_EmailLabel::text'
    path_affilation = '#DataList4_ctl%s_AffiliationLabel::text'
    get = lambda path: res.css(path).extract_first()
    value = []
    for ctl in ['01', '02']:
        value.append({
            'first_name': get(path_first_name % ctl),
            'last_name': get(path_last_name % ctl),
            'address': get(path_address % ctl),
            'telephone': get(path_telephone % ctl),
            'email': get(path_email % ctl),
            'affilation': get(path_affilation % ctl),
        })
    data[key] = value

    key = 'health_conditions_or_problems_studied'
    path = '//*[re:test(@id, "DataList8_ctl\d+_Condition_FreeTextLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'interventions'
    path = '//*[re:test(@id, "DataList10_ctl\d+_Intervention_FreeTextLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'primary_outcomes'
    path = '//*[re:test(@id, "DataList12_ctl\d+_Outcome_NameLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'secondary_outcomes'
    path = '//*[re:test(@id, "DataList14_ctl\d+_Outcome_NameLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'secondary_ids'
    path = '//*[re:test(@id, "DataList16_ctl\d+_SecondaryIDLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'sources_of_monetary_support'
    path = '//*[re:test(@id, "DataList18_ctl\d+_Source_NameLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    key = 'secondary_sponsors'
    path = '//*[re:test(@id, "DataList20_ctl\d+_Secondary_SponsorLabel")]/text()'
    value = res.xpath(path).extract()
    data[key] = value

    # Skip empty
    if not data['main_id']:
        logger.debug('No main_id: ICTRP - %s' % res.url)
        return None

    # Create record
    record = IctrpRecord.create(res.url, data)

    return record
