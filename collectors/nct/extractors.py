# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import xmltodict
from .record import NctRecord
logger = logging.getLogger(__name__)


# Module API

def extract_record(res):

    # Init data
    data = {}

    # General

    key = 'download_date'
    path = 'required_header/download_date'
    value = _extract_text(res, path)
    data[key] = value

    key = 'link_text'
    path = 'required_header/link_text'
    value = _extract_text(res, path)
    data[key] = value

    key = 'url'
    path = 'required_header/url'
    value = _extract_text(res, path)
    data[key] = value

    key = 'org_study_id'
    path = 'id_info/org_study_id'
    value = _extract_text(res, path)
    data[key] = value

    key = 'nct_id'
    path = 'id_info/nct_id'
    value = _extract_text(res, path)
    data[key] = value

    key = 'secondary_ids'
    path = 'id_info/secondary_id'
    value = _extract_list(res, path, expand='secondary_id')
    data[key] = value

    key = 'nct_aliases'
    path = 'id_info/nct_alias'
    value = _extract_list(res, path, expand='nct_alias')
    data[key] = value

    key = 'brief_title'
    path = 'brief_title'
    value = _extract_text(res, path)
    data[key] = value

    key = 'acronym'
    path = 'acronym'
    value = _extract_text(res, path)
    data[key] = value

    key = 'official_title'
    path = 'official_title'
    value = _extract_text(res, path)
    data[key] = value

    key = 'sponsors'
    path = 'sponsors/child::*'
    value = _extract_list(res, path)
    data[key] = value

    key = 'source'
    path = 'source'
    value = _extract_text(res, path)
    data[key] = value

    key = 'oversight_info'
    path = 'oversight_info'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'brief_summary'
    path = 'brief_summary/textblock'
    value = _extract_text(res, path)
    data[key] = value

    key = 'detailed_description'
    path = 'detailed_description/textblock'
    value = _extract_text(res, path)
    data[key] = value

    key = 'overall_status'
    path = 'overall_status'
    value = _extract_text(res, path)
    data[key] = value

    key = 'why_stopped'
    path = 'why_stopped'
    value = _extract_text(res, path)
    data[key] = value

    key = 'start_date'
    path = 'start_date'
    value = _extract_text(res, path)
    data[key] = value

    key = 'completion_date_actual'
    path = 'completion_date[@type="Actual"]'
    value = _extract_text(res, path)
    data[key] = value

    key = 'completion_date_anticipated'
    path = 'completion_date[@type="Actual"]'
    value = _extract_text(res, path)
    data[key] = value

    key = 'primary_completion_date_actual'
    path = 'primary_completion_date[@type="Actual"]'
    value = _extract_text(res, path)
    data[key] = value

    key = 'primary_completion_date_anticipated'
    path = 'primary_completion_date[@type="Actual"]'
    value = _extract_text(res, path)
    data[key] = value

    key = 'phase'
    path = 'phase'
    value = _extract_text(res, path)
    data[key] = value

    key = 'study_type'
    path = 'study_type'
    value = _extract_text(res, path)
    data[key] = value

    key = 'study_design'
    path = 'study_design'
    value = _extract_text(res, path)
    data[key] = value

    key = 'target_duration'
    path = 'target_duration'
    value = _extract_text(res, path)
    data[key] = value

    key = 'primary_outcomes'
    path = 'primary_outcome'
    value = _extract_list(res, path, expand='primary_outcome')
    data[key] = value

    key = 'secondary_outcomes'
    path = 'secondary_outcome'
    value = _extract_list(res, path, expand='secondary_outcome')
    data[key] = value

    key = 'other_outcomes'
    path = 'other_outcome'
    value = _extract_list(res, path, expand='other_outcome')
    data[key] = value

    key = 'number_of_arms'
    path = 'number_of_arms'
    value = _extract_text(res, path)
    data[key] = value

    key = 'number_of_groups'
    path = 'number_of_groups'
    value = _extract_text(res, path)
    data[key] = value

    key = 'enrollment_actual'
    path = 'enrollment[@type="Actual"]'
    value = _extract_text(res, path)
    data[key] = value

    key = 'enrollment_anticipated'
    path = 'enrollment[@type="Anticipated"]'
    value = _extract_text(res, path)
    data[key] = value

    key = 'conditions'
    path = 'condition'
    value = _extract_list(res, path, expand='condition')
    data[key] = value

    key = 'arm_groups'
    path = 'arm_group'
    value = _extract_list(res, path, expand='arm_group')
    data[key] = value

    key = 'interventions'
    path = 'intervention'
    value = _extract_list(res, path, expand='intervention')
    data[key] = value

    key = 'biospec_retention'
    path = 'biospec_retention'
    value = _extract_text(res, path)
    data[key] = value

    key = 'biospec_desrc'
    path = 'biospec_desrc/textblock'
    value = _extract_text(res, path)
    data[key] = value

    key = 'eligibility'
    path = 'eligibility'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'overall_officials'
    path = 'overall_official'
    value = _extract_list(res, path, expand='overall_official')
    data[key] = value

    key = 'overall_contact'
    path = 'overall_contact'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'overall_contact_backup'
    path = 'overall_contact_backup'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'locations'
    path = 'location'
    value = _extract_list(res, path, expand='location')
    data[key] = value

    key = 'location_countries'
    path = 'location_countries/child::*'
    value = _extract_list(res, path, expand='country')
    data[key] = value

    key = 'removed_countries'
    path = 'removed_countries/child::*'
    value = _extract_list(res, path, expand='country')
    data[key] = value

    key = 'links'
    path = 'link'
    value = _extract_list(res, path, expand='link')
    data[key] = value

    key = 'references'
    path = 'reference'
    value = _extract_list(res, path, expand='reference')
    data[key] = value

    key = 'results_references'
    path = 'results_reference'
    value = _extract_list(res, path, expand='results_reference')
    data[key] = value

    key = 'verification_date'
    path = 'verification_date'
    value = _extract_text(res, path)
    data[key] = value

    key = 'lastchanged_date'
    path = 'lastchanged_date'
    value = _extract_text(res, path)
    data[key] = value

    key = 'firstreceived_date'
    path = 'firstreceived_date'
    value = _extract_text(res, path)
    data[key] = value

    key = 'firstreceived_results_date'
    path = 'firstreceived_results_date'
    value = _extract_text(res, path)
    data[key] = value

    key = 'responsible_party'
    path = 'responsible_party'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'keywords'
    path = 'keyword'
    value = _extract_list(res, path, expand='keyword')
    data[key] = value

    key = 'is_fda_regulated'
    path = 'is_fda_regulated'
    value = _extract_text(res, path)
    data[key] = value

    key = 'is_section_801'
    path = 'is_section_801'
    value = _extract_text(res, path)
    data[key] = value

    key = 'has_expanded_access'
    path = 'has_expanded_access'
    value = _extract_text(res, path)
    data[key] = value

    key = 'condition_browse'
    path = 'condition_browse'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'intervention_browse'
    path = 'intervention_browse'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    key = 'clinical_results'
    path = 'clinical_results'
    value = _extract_dict(res, path, expand=key)
    data[key] = value

    # Create record
    record = NctRecord.create(res.url, data)

    return record


# Internal

def _extract_text(res, path):
    """Extract text from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            value = nodes.xpath('text()').extract_first()
            value = value.strip()
    except Exception as exception:
        message = 'Extraction error: %s: %s'
        message = message % (path, repr(exception))
        logger.warning(message)
    return value


def _extract_dict(res, path, expand=None):
    """Extract dict from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            text = nodes.extract_first()
            hash = xmltodict.parse(text)
            if expand:
                hash = hash[expand]
            value = hash
    except Exception as exception:
        message = 'Extraction error: %s: %s'
        message = message % (path, repr(exception))
        logger.warning(message)
    return value


def _extract_list(res, path, expand=None):
    """Extract list from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            hashs = []
            texts = nodes.extract()
            for text in texts:
                hash = xmltodict.parse(text)
                if expand:
                    hash = hash[expand]
                hashs.append(hash)
            value = hashs
    except Exception as exception:
        message = 'Extraction error: %s: %s'
        message = message % (path, repr(exception))
        logger.warning(message)
    return value
