# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy import Field

from .base import Base


# Module API

class Nct(Base):

    # Plain value fields

    download_date = Field()
    link_text = Field()
    url = Field()
    org_study_id = Field()
    nct_id = Field()
    brief_title = Field()
    acronym = Field()
    official_title = Field()
    source = Field()
    brief_summary = Field()
    detailed_description = Field()
    overall_status = Field()
    why_stopped = Field()
    start_date = Field()
    completion_date_actual = Field()
    completion_date_anticipated = Field()
    primary_completion_date_actual = Field()
    primary_completion_date_anticipated = Field()
    phase = Field()
    study_type = Field()
    study_design = Field()
    target_duration = Field()
    number_of_arms = Field()
    number_of_groups = Field()
    enrollment_actual = Field()
    enrollment_anticipated = Field()
    biospec_retention = Field()
    biospec_descr = Field()
    verification_date = Field()
    lastchanged_date = Field()
    firstreceived_date = Field()
    is_fda_regulated = Field()
    is_section_801 = Field()
    has_expanded_access = Field()

    # Dict value fields

    oversight_info = Field()
    eligibility = Field()
    overall_contact = Field()
    overall_contact_backup = Field()
    responsible_party = Field()
    clinical_results = Field()
    condition_browse = Field()
    intervention_browse = Field()

    # List value fields

    secondary_ids = Field()
    nct_aliases = Field()
    sponsors = Field()
    primary_outcomes = Field()
    secondary_outcomes = Field()
    other_outcomes = Field()
    conditions = Field()
    arm_groups = Field()
    interventions = Field()
    overall_officials = Field()
    locations = Field()
    location_countries = Field()
    removed_countries = Field()
    links = Field()
    references = Field()
    results_references = Field()
    keywords = Field()
