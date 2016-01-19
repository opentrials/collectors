# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy


class Item(scrapy.Item):

    # Plain value fields

    isrctn_id = scrapy.Field()
    scientific_title = scrapy.Field()
    reason_abandoned = scrapy.Field()
    participant_inclusion_criteria = scrapy.Field()
    sponsor_details = scrapy.Field()
    target_number_of_participants = scrapy.Field()
    sponsor_type = scrapy.Field()
    publication_summary = scrapy.Field()
    participant_type = scrapy.Field()
    funder_name = scrapy.Field()
    clinicaltrials_gov_number = scrapy.Field()
    primary_contact = scrapy.Field()
    age_group = scrapy.Field()
    participant_level_data = scrapy.Field()
    intervention = scrapy.Field()
    orcid_id = scrapy.Field()
    participant_exclusion_criteria = scrapy.Field()
    eudract_number = scrapy.Field()
    results_basic_reporting = scrapy.Field()
    organisation = scrapy.Field()
    recruitment_start_date = scrapy.Field()
    trial_setting = scrapy.Field()
    study_hypothesis = scrapy.Field()
    location = scrapy.Field()
    intention_to_publish_date = scrapy.Field()
    secondary_study_design = scrapy.Field()
    type = scrapy.Field()
    publication_and_dissemination_plan = scrapy.Field()
    website = scrapy.Field()
    contact_details = scrapy.Field()
    trial_type = scrapy.Field()
    acronym = scrapy.Field()
    funding_body_type = scrapy.Field()
    trial_participating_centre = scrapy.Field()
    plain_english_summary = scrapy.Field()
    protocol_serial_number = scrapy.Field()
    overall_trial_start_date = scrapy.Field()
    primary_study_design = scrapy.Field()
    phase = scrapy.Field()
    overall_trial_end_date = scrapy.Field()
    condition = scrapy.Field()
    trial_website = scrapy.Field()
    ethics_approval = scrapy.Field()
    study_design = scrapy.Field()
    countries_of_recruitment = scrapy.Field()
    intervention_type = scrapy.Field()
    funder_type = scrapy.Field()
    gender = scrapy.Field()
    primary_outcome_measures = scrapy.Field()
    recruitment_end_date = scrapy.Field()
    drug_names = scrapy.Field()
    secondary_outcome_measures = scrapy.Field()
    patient_information_sheet = scrapy.Field()
    funding_body_subtype = scrapy.Field()
    alternative_name_s_ = scrapy.Field()

    # Helpers

    def __repr__(self):
        return '<Item: "%s">' % self.get('isrctn_id')
