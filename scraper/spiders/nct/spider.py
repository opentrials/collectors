# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from functools import partial
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .item import Item
from .mapper import Mapper


# Module API

class Spider(base.Spider):

    # Public

    name = 'nct'
    allowed_domains = ['clinicaltrials.gov']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = Mapper()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='https://www.clinicaltrials.gov/ct2/results',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=utils.make_pattern('ct2/results'),
            )),
            Rule(LinkExtractor(
                allow=r'ct2/show/NCT\d+',
                process_value=lambda value: value+'&resultsxml=true',
            ), callback='parse_item'),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Init data
        data = {}

        # Extract download_date
        key = 'download_date'
        path = 'required_header/download_date'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract link_text
        key = 'link_text'
        path = 'required_header/link_text'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract url
        key = 'url'
        path = 'required_header/url'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract org_study_id
        key = 'org_study_id'
        path = 'id_info/org_study_id'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract nct_id
        key = 'nct_id'
        path = 'id_info/nct_id'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract brief_title
        key = 'brief_title'
        path = 'brief_title'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract acronym
        key = 'acronym'
        path = 'acronym'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract official_title
        key = 'official_title'
        path = 'official_title'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract source
        key = 'source'
        path = 'source'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract brief_summary
        key = 'brief_summary'
        path = 'brief_summary/textblock'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract detailed_description
        key = 'detailed_description'
        path = 'detailed_description/textblock'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract overall_status
        key = 'overall_status'
        path = 'overall_status'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract why_stopped
        key = 'why_stopped'
        path = 'why_stopped'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract start_date
        key = 'start_date'
        path = 'start_date'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract completion_date_actual
        key = 'completion_date_actual'
        path = 'completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract completion_date_anticipated
        key = 'completion_date_anticipated'
        path = 'completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract primary_completion_date_actual
        key = 'primary_completion_date_actual'
        path = 'primary_completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract primary_completion_date_anticipated
        key = 'primary_completion_date_anticipated'
        path = 'primary_completion_date[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract phase
        key = 'phase'
        path = 'phase'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract study_type
        key = 'study_type'
        path = 'study_type'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract study_design
        key = 'study_design'
        path = 'study_design'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract target_duration
        key = 'target_duration'
        path = 'target_duration'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract number_of_arms
        key = 'number_of_arms'
        path = 'number_of_arms'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract nuber_of_groups
        key = 'nuber_of_groups'
        path = 'nuber_of_groups'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract enrollment_actual
        key = 'enrollment_actual'
        path = 'enrollment[@type="Actual"]'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract enrollment_anticipated
        key = 'enrollment_anticipated'
        path = 'enrollment[@type="Anticipated"]'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract biospec_retention
        key = 'biospec_retention'
        path = 'biospec_retention'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract biospec_desrc
        key = 'biospec_desrc'
        path = 'biospec_desrc'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract verification_date
        key = 'verification_date'
        path = 'verification_date'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract lastchanged_date
        key = 'lastchanged_date'
        path = 'lastchanged_date'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract firstreceived_date
        key = 'firstreceived_date'
        path = 'firstreceived_date'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract is_fda_regulated
        key = 'is_fda_regulated'
        path = 'is_fda_regulated'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract is_section_801
        key = 'is_section_801'
        path = 'is_section_801'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract has_expanded_access
        key = 'has_expanded_access'
        path = 'has_expanded_access'
        value = utils.extract_text(res, path)
        data[key] = value

        # Extract oversight_info
        key = 'oversight_info'
        path = 'oversight_info'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract eligibility
        key = 'eligibility'
        path = 'eligibility'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract overall_contact
        key = 'overall_contact'
        path = 'overall_contact'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract overall_contact_backup
        key = 'overall_contact_backup'
        path = 'overall_contact_backup'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract resposible_party
        key = 'resposible_party'
        path = 'resposible_party'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract clinical_results
        key = 'clinical_results'
        path = 'clinical_results'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract condition_brows
        key = 'condition_brows'
        path = 'condition_brows'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract intervention_brows
        key = 'intervention_brows'
        path = 'intervention_brows'
        value = utils.extract_dict(res, path, expand=key)
        data[key] = value

        # Extract secondary_ids
        key = 'secondary_ids'
        path = 'id_info/secondary_id'
        value = utils.extract_list(res, path, expand='secondary_id')
        data[key] = value

        # Extract nct_aliases
        key = 'nct_aliases'
        path = 'id_info/nct_alias'
        value = utils.extract_list(res, path, expand='nct_alias')
        data[key] = value

        # Extract sponsors
        key = 'sponsors'
        path = 'sponsors/child::*'
        value = utils.extract_list(res, path)
        data[key] = value

        # Extract primary_outcomes
        key = 'primary_outcomes'
        path = 'primary_outcome'
        value = utils.extract_list(res, path, expand='primary_outcome')
        data[key] = value

        # Extract secondary_outcomes
        key = 'secondary_outcomes'
        path = 'secondary_outcome'
        value = utils.extract_list(res, path, expand='secondary_outcome')
        data[key] = value

        # Extract other_outcomes
        key = 'other_outcomes'
        path = 'other_outcome'
        value = utils.extract_list(res, path, expand='other_outcome')
        data[key] = value

        # Extract conditions
        key = 'conditions'
        path = 'condition'
        value = utils.extract_list(res, path, expand='condition')
        data[key] = value

        # Extract arm_groups
        key = 'arm_groups'
        path = 'arm_group'
        value = utils.extract_list(res, path, expand='arm_group')
        data[key] = value

        # Extract interventions
        key = 'interventions'
        path = 'intervention'
        value = utils.extract_list(res, path, expand='intervention')
        data[key] = value

        # Extract overall_officials
        key = 'overall_officials'
        path = 'overall_official'
        value = utils.extract_list(res, path, expand='overall_official')
        data[key] = value

        # Extract locations
        key = 'locations'
        path = 'location'
        value = utils.extract_list(res, path, expand='location')
        data[key] = value

        # Extract location_countries
        key = 'location_countries'
        path = 'location_countries/child::*'
        value = utils.extract_list(res, path, expand='country')
        data[key] = value

        # Extract removed_countries
        key = 'removed_countries'
        path = 'removed_countries/child::*'
        value = utils.extract_list(res, path, expand='country')
        data[key] = value

        # Extract links
        key = 'links'
        path = 'link'
        value = utils.extract_list(res, path, expand='link')
        data[key] = value

        # Extract references
        key = 'references'
        path = 'reference'
        value = utils.extract_list(res, path, expand='reference')
        data[key] = value

        # Extract results_references
        key = 'results_references'
        path = 'results_reference'
        value = utils.extract_list(res, path, expand='results_reference')
        data[key] = value

        # Extract keywords
        key = 'keywords'
        path = 'keyword'
        value = utils.extract_list(res, path, expand='keyword')
        data[key] = value

        # Create item, map and add data
        item = Item.create(source=res.url)
        data = self.mapper.map_data(data)
        item.add_data(data)

        return item
