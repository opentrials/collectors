# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy


class Item(scrapy.Item):

    # Plain value fields

    download_date = scrapy.Field()
    link_text = scrapy.Field()
    url = scrapy.Field()
    org_study_id = scrapy.Field()
    nct_id = scrapy.Field()
    brief_title = scrapy.Field()
    acronym = scrapy.Field()
    official_title = scrapy.Field()
    source = scrapy.Field()
    brief_summary = scrapy.Field()
    detailed_description = scrapy.Field()
    overall_status = scrapy.Field()
    why_stopped = scrapy.Field()
    start_date = scrapy.Field()
    completion_date_actual = scrapy.Field()
    completion_date_anticipated = scrapy.Field()
    primary_completion_date_actual = scrapy.Field()
    primary_completion_date_anticipated = scrapy.Field()
    phase = scrapy.Field()
    study_type = scrapy.Field()
    study_design = scrapy.Field()
    target_duration = scrapy.Field()
    number_of_arms = scrapy.Field()
    number_of_groups = scrapy.Field()
    enrollment_actual = scrapy.Field()
    enrollment_anticipated = scrapy.Field()
    biospec_retention = scrapy.Field()
    biospec_descr = scrapy.Field()
    verification_date = scrapy.Field()
    lastchanged_date = scrapy.Field()
    firstreceived_date = scrapy.Field()
    is_fda_regulated = scrapy.Field()
    is_section_801 = scrapy.Field()
    has_expanded_access = scrapy.Field()

    # Dict value fields

    oversight_info = scrapy.Field()
    eligibility = scrapy.Field()
    overall_contact = scrapy.Field()
    overall_contact_backup = scrapy.Field()
    responsible_party = scrapy.Field()
    clinical_results = scrapy.Field()
    condition_browse = scrapy.Field()
    intervention_browse = scrapy.Field()

    # List value fields

    secondary_ids = scrapy.Field()
    nct_aliases = scrapy.Field()
    sponsors = scrapy.Field()
    primary_outcomes = scrapy.Field()
    secondary_outcomes = scrapy.Field()
    other_outcomes = scrapy.Field()
    conditions = scrapy.Field()
    arm_groups = scrapy.Field()
    interventions = scrapy.Field()
    overall_officials = scrapy.Field()
    locations = scrapy.Field()
    location_countries = scrapy.Field()
    removed_countries = scrapy.Field()
    links = scrapy.Field()
    references = scrapy.Field()
    results_references = scrapy.Field()
    keywords = scrapy.Field()
