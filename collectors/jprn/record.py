# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean, Integer, Array, Datetime


# Module API

class JprnRecord(base.Record):

    # Config

    table = 'jprn'
    primary_key = 'unique_trial_number'
    updated_key = 'date_and_time_of_last_update'
    ensure_fields = False

    # General

    recruitment_status = Text()
    unique_trial_number = Text()
    title_of_the_study = Text()
    date_of_formal_registrationdate_of_icmje_and_who = Date('%Y/%m/%d')
    date_and_time_of_last_update = Datetime('%Y/%m/%d %H:%M:%S')

    # Basic information

    official_scientific_title_of_the_study = Text()
    title_of_the_study_brief_title = Text()
    region = Text()

    # Condition

    condition = Text()
    classification_by_specialty = Text()
    classification_by_malignancy = Text()
    genomic_information = Boolean('YES')

    # Objectives

    narrative_objectives1 = Text()
    basic_objectives2 = Text()
    basic_objectives_others = Text()
    trial_characteristics_1 = Text()
    trial_characteristics_2 = Text()
    developmental_phase = Text()

    # Assessment

    primary_outcomes = Text()
    key_secondary_outcomes = Text()

    # Base

    study_type = Text()

    # Study design

    basic_design = Text()
    randomization = Text()
    randomization_unit = Text()
    blinding = Text()
    control = Text()
    stratification = Text()
    dynamic_allocation = Text()
    institution_consideration = Text()
    blocking = Text()
    concealment = Text()

    # Intervention

    no_of_arms = Integer()
    purpose_of_intervention = Text()
    type_of_intervention = Text()
    interventions = Array()

    # Eligibility

    agelower_limit = Text()
    ageupper_limit = Text()
    gender = Text()
    key_inclusion_criteria = Text()
    key_exclusion_criteria = Text()
    target_sample_size = Integer()

    # Research contact person

    research_name_of_lead_principal_investigator = Text()
    research_organization = Text()
    research_division_name = Text()
    research_address = Text()
    research_tel = Text()
    research_homepage_url = Text()
    research_email = Text()

    # Public contact

    public_name_of_contact_person = Text()
    public_organization = Text()
    public_division_name = Text()
    public_address = Text()
    public_tel = Text()
    public_homepage_url = Text()
    public_email = Text()

    # Sponsor

    name_of_primary_sponsor = Text()

    # Funding source

    source_of_funding = Text()
    category_of_org = Text()
    nation_of_funding = Text()

    # Other related organizations

    cosponsor = Text()
    name_of_secondary_funers = Text()

    # Secondary study IDs

    secondary_study_ids = Boolean('YES')
    secondary_study_id_1 = Text()
    org_issuing_secondary_study_id_1 = Text()
    secondary_study_id_2 = Text()
    org_issuing_secondary_study_id_2 = Text()
    ind_to_mhlw = Text()

    # Institutions

    institutions = Text()

    # Progress

    recruitment_status = Text()
    date_of_protocol_fixation = Date('%Y/%m/%d')
    anticipated_trial_start_date = Date('%Y/%m/%d')
    last_followup_date = Date('%Y/%m/%d')
    date_of_closure_to_data_entry = Date('%Y/%m/%d')
    date_trial_data_considered_complete = Date('%Y/%m/%d')
    date_analysis_concluded = Date('%Y/%m/%d')

    # Related information

    url_releasing_protocol = Text()
    publication_of_results = Text()
    url_releasing_results = Text()
    results = Text()
    other_related_information = Text()

    # Others

    date_of_registration = Date('%Y/%m/%d')
    date_of_last_update = Datetime('%Y/%m/%d %H:%M:%S')
    urljapanese = Text()
    urlenglish = Text()
