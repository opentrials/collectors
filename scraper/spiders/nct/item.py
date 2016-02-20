# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Integer, Json, Array, Boolean


# Module API

class Item(base.Item):

    # Config

    table = 'nct'
    primary_key = 'nct_id'
    updated_key = 'lastchanged_date'
    ensure_fields = False

    # General

    download_date = Text()
    link_text = Text()
    url = Text()
    org_study_id = Text()
    nct_id = Text()
    secondary_ids = Array()
    nct_aliases = Array()
    brief_title = Text()
    acronym = Text()
    official_title = Text()
    sponsors = Json()
    source = Text()
    oversight_info = Json()
    brief_summary = Text()
    detailed_description = Text()
    overall_status = Text()
    why_stopped = Text()
    start_date = Date('%B %Y')
    completion_date_actual = Date('%B %Y')
    completion_date_anticipated = Date('%B %Y')
    primary_completion_date_actual = Date('%B %Y')
    primary_completion_date_anticipated = Date('%B %Y')
    phase = Text()
    study_type = Text()
    study_design = Text()
    target_duration = Text()
    primary_outcomes = Json()
    secondary_outcomes = Json()
    other_outcomes = Json()
    number_of_arms = Integer()
    number_of_groups = Integer()
    enrollment_actual = Integer()
    enrollment_anticipated = Integer()
    conditions = Array()
    arm_groups = Json()
    interventions = Json()
    biospec_retention = Text()
    biospec_desrc = Text()
    eligibility = Json()
    overall_officials = Json()
    overall_contact = Json()
    overall_contact_backup = Json()
    locations = Json()
    location_countries = Array()
    removed_countries = Array()
    links = Json()
    references = Json()
    results_references = Json()
    verification_date = Date('%B %Y')
    lastchanged_date = Date('%B %d, %Y')
    firstreceived_date = Date('%B %d, %Y')
    firstreceived_results_date = Date('%B %d, %Y')
    responsible_party = Json()
    keywords = Array()
    is_fda_regulated = Boolean('Yes')
    is_section_801 = Boolean('Yes')
    has_expanded_access = Boolean('Yes')
    condition_browse = Json()
    intervention_browse = Json()
    clinical_results = Json()
