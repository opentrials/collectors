# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .item import Item


# Module API

class Mapper(base.Mapper):

    # Public

    def map_response(self, res):

        # Init data
        data = {}

        # General

        key = 'download_date'
        path = 'required_header/download_date'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'link_text'
        path = 'required_header/link_text'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'url'
        path = 'required_header/url'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'org_study_id'
        path = 'id_info/org_study_id'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'nct_id'
        path = 'id_info/nct_id'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'secondary_ids'
        path = 'id_info/secondary_id'
        value = utils.extract_list(res, path, expand='secondary_id')
        data[key] = value

        key = 'nct_aliases'
        path = 'id_info/nct_alias'
        value = utils.extract_list(res, path, expand='nct_alias')
        data[key] = value

        key = 'brief_title'
        path = 'brief_title'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'acronym'
        path = 'acronym'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'official_title'
        path = 'official_title'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'sponsors'
        path = 'sponsors/child::*'
        value = utils.extract_list(res, path)
        data[key] = value

        key = 'source'
        path = 'source'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'oversight_info'
        path = 'oversight_info'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'brief_summary'
        path = 'brief_summary/textblock'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'detailed_description'
        path = 'detailed_description/textblock'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'overall_status'
        path = 'overall_status'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'why_stopped'
        path = 'why_stopped'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'start_date'
        path = 'start_date'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'completion_date_actual'
        path = 'completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'completion_date_anticipated'
        path = 'completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'primary_completion_date_actual'
        path = 'primary_completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'primary_completion_date_anticipated'
        path = 'primary_completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'phase'
        path = 'phase'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'study_type'
        path = 'study_type'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'study_design'
        path = 'study_design'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'target_duration'
        path = 'target_duration'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'primary_outcomes'
        path = 'primary_outcome'
        value = utils.extract_list(res, path, expand='primary_outcome')
        data[key] = value

        key = 'secondary_outcomes'
        path = 'secondary_outcome'
        value = utils.extract_list(res, path, expand='secondary_outcome')
        data[key] = value

        key = 'other_outcomes'
        path = 'other_outcome'
        value = utils.extract_list(res, path, expand='other_outcome')
        data[key] = value

        key = 'number_of_arms'
        path = 'number_of_arms'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'number_of_groups'
        path = 'number_of_groups'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'enrollment_actual'
        path = 'enrollment[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'enrollment_anticipated'
        path = 'enrollment[@type="Anticipated"]'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'conditions'
        path = 'condition'
        value = utils.extract_list(res, path, expand='condition')
        data[key] = value

        key = 'arm_groups'
        path = 'arm_group'
        value = utils.extract_list(res, path, expand='arm_group')
        data[key] = value

        key = 'interventions'
        path = 'intervention'
        value = utils.extract_list(res, path, expand='intervention')
        data[key] = value

        key = 'biospec_retention'
        path = 'biospec_retention'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'biospec_desrc'
        path = 'biospec_desrc/textblock'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'eligibility'
        path = 'eligibility'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'overall_officials'
        path = 'overall_official'
        value = utils.extract_list(res, path, expand='overall_official')
        data[key] = value

        key = 'overall_contact'
        path = 'overall_contact'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'overall_contact_backup'
        path = 'overall_contact_backup'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'locations'
        path = 'location'
        value = utils.extract_list(res, path, expand='location')
        data[key] = value

        key = 'location_countries'
        path = 'location_countries/child::*'
        value = utils.extract_list(res, path, expand='country')
        data[key] = value

        key = 'removed_countries'
        path = 'removed_countries/child::*'
        value = utils.extract_list(res, path, expand='country')
        data[key] = value

        key = 'links'
        path = 'link'
        value = utils.extract_list(res, path, expand='link')
        data[key] = value

        key = 'references'
        path = 'reference'
        value = utils.extract_list(res, path, expand='reference')
        data[key] = value

        key = 'results_references'
        path = 'results_reference'
        value = utils.extract_list(res, path, expand='results_reference')
        data[key] = value

        key = 'verification_date'
        path = 'verification_date'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'lastchanged_date'
        path = 'lastchanged_date'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'firstreceived_date'
        path = 'firstreceived_date'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'firstreceived_results_date'
        path = 'firstreceived_results_date'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'responsible_party'
        path = 'responsible_party'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'keywords'
        path = 'keyword'
        value = utils.extract_list(res, path, expand='keyword')
        data[key] = value

        key = 'is_fda_regulated'
        path = 'is_fda_regulated'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'is_section_801'
        path = 'is_section_801'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'has_expanded_access'
        path = 'has_expanded_access'
        value = utils.extract_text(res, path)
        data[key] = value

        key = 'condition_browse'
        path = 'condition_browse'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'intervention_browse'
        path = 'intervention_browse'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        key = 'clinical_results'
        path = 'clinical_results'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Create item
        item = Item.create(res.url, data)

        return item
