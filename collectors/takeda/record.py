# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Integer, Array


# Module API

class Record(base.Record):

    # Config

    table = 'takeda'

    # General

    takeda_trial_id = Text(primary_key=True)
    official_title = Text()
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
    trial_arms_groups_or_cohorts = Text()

    # Recruitment

    gender = Text()
    ages = Text()
    enrollment_number_of_participants = Integer()
    locations = Array()
    responsible_party = Text()
    trial_sponsor = Text()
    start_date = Date('%B %Y')
    completion_date = Date('%B %Y')
    eligibility_criteria = Text()

    # Results

    download_the_clinical_trial_summary = Text()
    other_available_languages = Text()
