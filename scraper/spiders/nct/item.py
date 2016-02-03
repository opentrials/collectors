# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from scrapy import Field
from sqlalchemy.dialects.postgresql import ARRAY, JSON

from .. import base


# Module API

class Item(base.Item):

    # Config

    table = 'nct'
    primary_key = 'nct_id'
    updated_key = 'lastchanged_date'

    # General

    download_date = Field()
    link_text = Field()
    url = Field()
    org_study_id = Field()
    nct_id = Field()
    secondary_ids = Field(type=ARRAY(sa.Text))
    nct_aliases = Field(type=ARRAY(sa.Text))
    brief_title = Field()
    acronym = Field()
    official_title = Field()
    sponsors = Field(type=JSON)
    source = Field()
    oversight_info = Field(type=JSON)
    brief_summary = Field()
    detailed_description = Field()
    overall_status = Field()
    why_stopped = Field()
    start_date = Field(type=sa.Date)
    completion_date_actual = Field(type=sa.Date)
    completion_date_anticipated = Field(type=sa.Date)
    primary_completion_date_actual = Field(type=sa.Date)
    primary_completion_date_anticipated = Field(type=sa.Date)
    phase = Field()
    study_type = Field()
    study_design = Field()
    target_duration = Field()
    primary_outcomes = Field(type=JSON)
    secondary_outcomes = Field(type=JSON)
    other_outcomes = Field(type=JSON)
    number_of_arms = Field(type=sa.Integer)
    number_of_groups = Field(type=sa.Integer)
    enrollment_actual = Field(type=sa.Integer)
    enrollment_anticipated = Field(type=sa.Integer)
    conditions = Field(type=ARRAY(sa.Text))
    arm_groups = Field(type=JSON)
    interventions = Field(type=JSON)
    biospec_retention = Field()
    biospec_desrc = Field()
    eligibility = Field(type=JSON)
    overall_officials = Field(type=JSON)
    overall_contact = Field(type=JSON)
    overall_contact_backup = Field(type=JSON)
    locations = Field(type=JSON)
    location_countries = Field(type=ARRAY(sa.Text))
    removed_countries = Field(type=ARRAY(sa.Text))
    links = Field(type=JSON)
    references = Field(type=JSON)
    results_references = Field(type=JSON)
    verification_date = Field(type=sa.Date)
    lastchanged_date = Field(type=sa.Date)
    firstreceived_date = Field(type=sa.Date)
    firstreceived_results_date = Field(type=sa.Date)
    responsible_party = Field(type=JSON)
    keywords = Field(type=ARRAY(sa.Text))
    is_fda_regulated = Field()
    is_section_801 = Field()
    has_expanded_access = Field()
    condition_browse = Field(type=JSON)
    intervention_browse = Field(type=JSON)
    clinical_results = Field(type=JSON)
