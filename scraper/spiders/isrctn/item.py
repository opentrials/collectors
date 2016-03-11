# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Json


# Module API

class Item(base.Item):

    # Config

    table = 'data_isrctn'
    primary_key = 'isrctn_id'
    updated_key = 'last_edited'
    ensure_fields = False

    # General

    isrctn_id = Text()
    doi_isrctn_id = Text()
    title = Text()
    condition_category = Text()
    date_applied = Date('%d/%m/%Y')
    date_assigned = Date('%d/%m/%Y')
    last_edited = Date('%d/%m/%Y')
    prospectiveretrospective = Text()
    overall_trial_status = Text()
    recruitment_status = Text()
    plain_english_summary = Text()
    trial_website = Text()

    # Contant information

    contacts = Json()

    # Additional identifiers

    eudract_number = Text()
    clinicaltrialsgov_number = Text()
    protocolserial_number = Text()

    # Study information

    scientific_title = Text()
    acronym = Text()
    study_hypothesis = Text()
    ethics_approval = Text()
    study_design = Text()
    primary_study_design = Text()
    secondary_study_design = Text()
    trial_setting = Text()
    trial_type = Text()
    patient_information_sheet = Text()
    condition = Text()
    intervention = Text()
    intervention_type = Text()
    phase = Text()
    drug_names = Text()
    primary_outcome_measures = Text()
    secondary_outcome_measures = Text()
    overall_trial_start_date = Date('%d/%m/%Y')
    overall_trial_end_date = Date('%d/%m/%Y')
    reason_abandoned = Text()

    # Eligability

    participant_inclusion_criteria = Text()
    participant_type = Text()
    age_group = Text()
    gender = Text()
    target_number_of_participants = Text()
    participant_exclusion_criteria = Text()
    recruitment_start_date = Date('%d/%m/%Y')
    recruitment_end_date = Date('%d/%m/%Y')

    # Locations

    countries_of_recruitment = Text()
    trial_participating_centre = Text()

    # Sponsor information

    sponsors = Json()

    # Funders

    funders = Json()

    # Results and publications

    publication_and_dissemination_plan = Text()
    intention_to_publish_date = Date('%d/%m/%Y')
    participant_level_data = Text()
    results_basic_reporting = Text()
    publication_summary = Text()
    publication_citations = Text()

    # Additional files

    # ...

    # Editorial notes

    # ...
