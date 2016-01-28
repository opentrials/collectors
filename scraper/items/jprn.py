# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy import Field

from .base import Base


# Module API

class Jprn(Base):

    # Config

    primary_key = 'unique_trial_number'
    updated_key = 'date_and_time_of_last_update'

    # Plain value fields

    recruitment_status = Field()
    unique_trial_number = Field()
    title_of_the_study = Field()
    date_of_formal_registrationdate_of_icmje_and_who = Field()
    date_and_time_of_last_update = Field()
    official_scientific_title_of_the_study = Field()
    title_of_the_study_brief_title = Field()
    region = Field()
    condition = Field()
    classification_by_specialty = Field()
    classification_by_malignancy = Field()
    genomic_information = Field()
    narrative_objectives1 = Field()
    basic_objectives2 = Field()
    basic_objectives_others = Field()
    trial_characteristics_1 = Field()
    trial_characteristics_2 = Field()
    developmental_phase = Field()
    primary_outcomes = Field()
    key_secondary_outcomes = Field()
    study_type = Field()
    basic_design = Field()
    randomization = Field()
    randomization_unit = Field()
    blinding = Field()
    control = Field()
    stratification = Field()
    dynamic_allocation = Field()
    institution_consideration = Field()
    blocking = Field()
    concealment = Field()
    no_of_arms = Field()
    purpose_of_intervention = Field()
    type_of_intervention = Field()
    interventionscontrol_1 = Field()
    interventionscontrol_2 = Field()
    interventionscontrol_3 = Field()
    interventionscontrol_4 = Field()
    interventionscontrol_5 = Field()
    interventionscontrol_6 = Field()
    interventionscontrol_7 = Field()
    interventionscontrol_8 = Field()
    interventionscontrol_9 = Field()
    interventionscontrol_10 = Field()
    agelower_limit = Field()
    ageupper_limit = Field()
    gender = Field()
    key_inclusion_criteria = Field()
    key_exclusion_criteria = Field()
    target_sample_size = Field()
    name_of_lead_principal_investigator = Field()
    organization = Field()
    division_name = Field()
    address = Field()
    tel = Field()
    email = Field()
    name_of_contact_person = Field()
    organization = Field()
    division_name = Field()
    address = Field()
    tel = Field()
    homepage_url = Field()
    email = Field()
    name_of_primary_sponsor = Field()
    source_of_funding = Field()
    category_of_org = Field()
    nation_of_funding = Field()
    secondary_study_ids = Field()
    secondary_study_id_1 = Field()
    org_issuing_secondary_study_id_1 = Field()
    secondary_study_id_2 = Field()
    org_issuing_secondary_study_id_2 = Field()
    ind_to_mhlw = Field()
    institutions = Field()
    recruitment_status = Field()
    date_of_protocol_fixation = Field()
    anticipated_trial_start_date = Field()
    last_followup_date = Field()
    date_of_closure_to_data_entry = Field()
    date_trial_data_considered_complete = Field()
    date_analysis_concluded = Field()
    url_releasing_protocol = Field()
    publication_of_results = Field()
    url_releasing_results = Field()
    results = Field()
    other_related_information = Field()
    date_of_registration = Field()
    date_of_last_update = Field()
    urljapanese = Field()
    urlenglish = Field()
