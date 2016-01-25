# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy


# Module API

class Jprn(scrapy.Item):

    # Plain value fields

    recruitment_status = scrapy.Field()
    unique_trial_number = scrapy.Field()
    title_of_the_study = scrapy.Field()
    date_of_formal_registrationdate_of_icmje_and_who = scrapy.Field()
    date_and_time_of_last_update = scrapy.Field()
    official_scientific_title_of_the_study = scrapy.Field()
    title_of_the_study_brief_title = scrapy.Field()
    region = scrapy.Field()
    condition = scrapy.Field()
    classification_by_specialty = scrapy.Field()
    classification_by_malignancy = scrapy.Field()
    genomic_information = scrapy.Field()
    narrative_objectives1 = scrapy.Field()
    basic_objectives2 = scrapy.Field()
    basic_objectives_others = scrapy.Field()
    trial_characteristics_1 = scrapy.Field()
    trial_characteristics_2 = scrapy.Field()
    developmental_phase = scrapy.Field()
    primary_outcomes = scrapy.Field()
    key_secondary_outcomes = scrapy.Field()
    study_type = scrapy.Field()
    basic_design = scrapy.Field()
    randomization = scrapy.Field()
    randomization_unit = scrapy.Field()
    blinding = scrapy.Field()
    control = scrapy.Field()
    stratification = scrapy.Field()
    dynamic_allocation = scrapy.Field()
    institution_consideration = scrapy.Field()
    blocking = scrapy.Field()
    concealment = scrapy.Field()
    no_of_arms = scrapy.Field()
    purpose_of_intervention = scrapy.Field()
    type_of_intervention = scrapy.Field()
    interventionscontrol_1 = scrapy.Field()
    interventionscontrol_2 = scrapy.Field()
    interventionscontrol_3 = scrapy.Field()
    interventionscontrol_4 = scrapy.Field()
    interventionscontrol_5 = scrapy.Field()
    interventionscontrol_6 = scrapy.Field()
    interventionscontrol_7 = scrapy.Field()
    interventionscontrol_8 = scrapy.Field()
    interventionscontrol_9 = scrapy.Field()
    interventionscontrol_10 = scrapy.Field()
    agelower_limit = scrapy.Field()
    ageupper_limit = scrapy.Field()
    gender = scrapy.Field()
    key_inclusion_criteria = scrapy.Field()
    key_exclusion_criteria = scrapy.Field()
    target_sample_size = scrapy.Field()
    name_of_lead_principal_investigator = scrapy.Field()
    organization = scrapy.Field()
    division_name = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    email = scrapy.Field()
    name_of_contact_person = scrapy.Field()
    organization = scrapy.Field()
    division_name = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    homepage_url = scrapy.Field()
    email = scrapy.Field()
    name_of_primary_sponsor = scrapy.Field()
    source_of_funding = scrapy.Field()
    category_of_org = scrapy.Field()
    nation_of_funding = scrapy.Field()
    secondary_study_ids = scrapy.Field()
    secondary_study_id_1 = scrapy.Field()
    org_issuing_secondary_study_id_1 = scrapy.Field()
    secondary_study_id_2 = scrapy.Field()
    org_issuing_secondary_study_id_2 = scrapy.Field()
    ind_to_mhlw = scrapy.Field()
    institutions = scrapy.Field()
    recruitment_status = scrapy.Field()
    date_of_protocol_fixation = scrapy.Field()
    anticipated_trial_start_date = scrapy.Field()
    last_followup_date = scrapy.Field()
    date_of_closure_to_data_entry = scrapy.Field()
    date_trial_data_considered_complete = scrapy.Field()
    date_analysis_concluded = scrapy.Field()
    url_releasing_protocol = scrapy.Field()
    publication_of_results = scrapy.Field()
    url_releasing_results = scrapy.Field()
    results = scrapy.Field()
    other_related_information = scrapy.Field()
    date_of_registration = scrapy.Field()
    date_of_last_update = scrapy.Field()
    urljapanese = scrapy.Field()
    urlenglish = scrapy.Field()

    # Helpers

    def __repr__(self):
        template = '<JPRN: %s [%s]>'
        text = template % (
                self.get('unique_trial_number'),
                self.get('date_and_time_of_last_update'))
        return text

    def add_data(self, key, value):
        if key in self.fields:
            self[key] = value
