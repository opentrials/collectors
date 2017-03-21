# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import xmltodict
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
from .record import Record
logger = logging.getLogger(__name__)


# Module API

def parse_record(res):

    # Init data
    data = {}
    res = etree.parse(res)
    # General

    key = 'download_date'
    path = 'required_header/download_date'
    value = _parse_text(res, path)
    data[key] = value

    key = 'link_text'
    path = 'required_header/link_text'
    value = _parse_text(res, path)
    data[key] = value

    key = 'url'
    path = 'required_header/url'
    value = _parse_text(res, path)
    data[key] = value

    key = 'org_study_id'
    path = 'id_info/org_study_id'
    value = _parse_text(res, path)
    data[key] = value

    key = 'nct_id'
    path = 'id_info/nct_id'
    value = _parse_text(res, path)
    data[key] = value

    key = 'secondary_ids'
    path = 'id_info/secondary_id'
    value = _parse_list(res, path, expand='secondary_id')
    data[key] = value

    key = 'nct_aliases'
    path = 'id_info/nct_alias'
    value = _parse_list(res, path, expand='nct_alias')
    data[key] = value

    key = 'brief_title'
    path = 'brief_title'
    value = _parse_text(res, path)
    data[key] = value

    key = 'acronym'
    path = 'acronym'
    value = _parse_text(res, path)
    data[key] = value

    key = 'official_title'
    path = 'official_title'
    value = _parse_text(res, path)
    data[key] = value

    key = 'sponsors'
    path = 'sponsors/*'
    value = _parse_list(res, path)
    data[key] = value

    key = 'source'
    path = 'source'
    value = _parse_text(res, path)
    data[key] = value

    key = 'oversight_info'
    path = 'oversight_info'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'brief_summary'
    path = 'brief_summary/textblock'
    value = _parse_text(res, path)
    data[key] = value

    key = 'detailed_description'
    path = 'detailed_description/textblock'
    value = _parse_text(res, path)
    data[key] = value

    key = 'overall_status'
    path = 'overall_status'
    value = _parse_text(res, path)
    data[key] = value

    key = 'why_stopped'
    path = 'why_stopped'
    value = _parse_text(res, path)
    data[key] = value

    key = 'start_date'
    path = 'start_date'
    value = _parse_text(res, path)
    data[key] = value

    key = 'completion_date_actual'
    path = 'completion_date[@type="Actual"]'
    value = _parse_text(res, path)
    data[key] = value

    key = 'completion_date_anticipated'
    path = 'completion_date[@type="Actual"]'
    value = _parse_text(res, path)
    data[key] = value

    key = 'primary_completion_date_actual'
    path = 'primary_completion_date[@type="Actual"]'
    value = _parse_text(res, path)
    data[key] = value

    key = 'primary_completion_date_anticipated'
    path = 'primary_completion_date[@type="Actual"]'
    value = _parse_text(res, path)
    data[key] = value

    key = 'phase'
    path = 'phase'
    value = _parse_text(res, path)
    data[key] = value

    key = 'study_type'
    path = 'study_type'
    value = _parse_text(res, path)
    data[key] = value

    key = 'study_design'
    path = 'study_design'
    value = _parse_text(res, path)
    data[key] = value

    key = 'target_duration'
    path = 'target_duration'
    value = _parse_text(res, path)
    data[key] = value

    key = 'primary_outcomes'
    path = 'primary_outcome'
    value = _parse_list(res, path, expand='primary_outcome')
    data[key] = value

    key = 'secondary_outcomes'
    path = 'secondary_outcome'
    value = _parse_list(res, path, expand='secondary_outcome')
    data[key] = value

    key = 'other_outcomes'
    path = 'other_outcome'
    value = _parse_list(res, path, expand='other_outcome')
    data[key] = value

    key = 'number_of_arms'
    path = 'number_of_arms'
    value = _parse_text(res, path)
    data[key] = value

    key = 'number_of_groups'
    path = 'number_of_groups'
    value = _parse_text(res, path)
    data[key] = value

    key = 'enrollment_actual'
    path = 'enrollment[@type="Actual"]'
    value = _parse_text(res, path)
    data[key] = value

    key = 'enrollment_anticipated'
    path = 'enrollment[@type="Anticipated"]'
    value = _parse_text(res, path)
    data[key] = value

    key = 'conditions'
    path = 'condition'
    value = _parse_list(res, path, expand='condition')
    data[key] = value

    key = 'arm_groups'
    path = 'arm_group'
    value = _parse_list(res, path, expand='arm_group')
    data[key] = value

    key = 'interventions'
    path = 'intervention'
    value = _parse_list(res, path, expand='intervention')
    data[key] = value

    key = 'biospec_retention'
    path = 'biospec_retention'
    value = _parse_text(res, path)
    data[key] = value

    key = 'biospec_desrc'
    path = 'biospec_desrc/textblock'
    value = _parse_text(res, path)
    data[key] = value

    key = 'eligibility'
    path = 'eligibility'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'overall_officials'
    path = 'overall_official'
    value = _parse_list(res, path, expand='overall_official')
    data[key] = value

    key = 'overall_contact'
    path = 'overall_contact'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'overall_contact_backup'
    path = 'overall_contact_backup'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'locations'
    path = 'location'
    value = _parse_list(res, path, expand='location')
    data[key] = value

    key = 'location_countries'
    path = 'location_countries/*'
    value = _parse_list(res, path, expand='country')
    data[key] = value

    key = 'removed_countries'
    path = 'removed_countries/*'
    value = _parse_list(res, path, expand='country')
    data[key] = value

    key = 'links'
    path = 'link'
    value = _parse_list(res, path, expand='link')
    data[key] = value

    key = 'references'
    path = 'reference'
    value = _parse_list(res, path, expand='reference')
    data[key] = value

    key = 'results_references'
    path = 'results_reference'
    value = _parse_list(res, path, expand='results_reference')
    data[key] = value

    key = 'verification_date'
    path = 'verification_date'
    value = _parse_text(res, path)
    data[key] = value

    key = 'lastchanged_date'
    path = 'lastchanged_date'
    value = _parse_text(res, path)
    data[key] = value

    key = 'firstreceived_date'
    path = 'firstreceived_date'
    value = _parse_text(res, path)
    data[key] = value

    key = 'firstreceived_results_date'
    path = 'firstreceived_results_date'
    value = _parse_text(res, path)
    data[key] = value

    key = 'responsible_party'
    path = 'responsible_party'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'keywords'
    path = 'keyword'
    value = _parse_list(res, path, expand='keyword')
    data[key] = value

    key = 'is_fda_regulated'
    path = 'is_fda_regulated'
    value = _parse_text(res, path)
    data[key] = value

    key = 'is_section_801'
    path = 'is_section_801'
    value = _parse_text(res, path)
    data[key] = value

    key = 'has_expanded_access'
    path = 'has_expanded_access'
    value = _parse_text(res, path)
    data[key] = value

    key = 'condition_browse'
    path = 'condition_browse'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'intervention_browse'
    path = 'intervention_browse'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'clinical_results'
    path = 'clinical_results'
    value = _parse_dict(res, path, expand=key)
    data[key] = value

    key = 'results_exemption_date'
    path = 'firstreceived_results_disposition_date'
    value = _parse_text(res, path)
    data[key] = value

    # Create record
    url = 'https://clinicaltrials.gov/ct2/show/%s' % data['nct_id']
    record = Record.create(url, data)

    return record


# Internal

def _parse_text(res, path):
    """Parsing text from response by path.
    """
    value = None
    node = res.find(path)
    if node is not None:
        value = node.text
        value = value.strip()
    return value


def _parse_dict(res, path, expand=None):
    """Parse dict from response by path.
    """
    value = None
    node = res.find(path)
    if node is not None:
        text = etree.tostring(node, encoding='utf-8', method='xml')
        node_dict = xmltodict.parse(text)
        if expand:
            node_dict = node_dict[expand]
        value = node_dict
    return value


def _parse_list(res, path, expand=None):
    """Parse list from response by path.
    """
    value = None
    nodes = res.findall(path)
    if len(nodes) > 0:
        hashs = []
        for node in nodes:
            text = etree.tostring(node, encoding='utf-8', method='xml')
            node_dict = xmltodict.parse(text)
            if expand:
                node_dict = node_dict[expand]
            hashs.append(node_dict)
        value = hashs
    return value
