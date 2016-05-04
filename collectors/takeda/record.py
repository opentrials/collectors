# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Integer, Array


# Module API

class TakedaRecord(base.Record):

    # Config

    table = 'takeda'
    primary_key = 'takeda_trial_id'
    updated_key = None
    ensure_fields = False

    # General

    official_title = Text()
    takeda_trial_id = Text()
    trial_phase = Text()
    condition = Text()
    compound = Array()
    recruitment_status = Text()

    # Description

    nct_number = Text()
    trial_type = Text()
    other_trial_ids = Text()
    acronym = Text()
    brief_summary = Text()
    detailed_description = Text()
    trial_design = Text()
    primary_outcome_measures = Text()
    secondary_outcome_measures = Text()
    trial_armsgroups_or_cohorts = Text()

    # Recruitment

    gender = Text()
    ages = Text()
    enrollmentnumber_of_participants = Integer()
    locations = Array()
    responsible_party = Text()
    trial_sponsor = Text()
    start_date = Date('%B %Y')
    completion_date = Date('%B %Y')
    eligibility_criteria = Text()

    # Results

    download_the_clinical_trial_summary = Text()
    other_available_languages = Text()
