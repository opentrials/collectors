# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from scrapy import Field
from sqlalchemy.dialects.postgresql import JSON

from .. import base


# Module API

class Item(base.Item):

    # Config

    table = 'euctr'
    primary_key = 'eudract_number_with_country'
    updated_key = 'date_on_which_this_record_was_first_entered'

    # Summary

    eudract_number_with_country = Field()
    eudract_number = Field()
    sponsors_protocol_code_number = Field()
    national_competent_authority = Field()
    clinical_trial_type = Field()
    trial_status = Field()
    date_on_which_this_record_was_first_entered = Field(type=sa.Date)
    trial_results = Field()

    # Protocol Information (Section A)

    member_state_concerned = Field()
    full_title_of_the_trial = Field()
    title_of_the_trial_for_lay_people_in = Field()
    name_or_abbreviated_title_of_the_trial_where = Field()
    sponsors_protocol_code_number = Field()
    isrctn_international_standard_randomised_controlled_trial_number = Field()
    trial_is_part_of_a_paediatric_investigation_plan = Field()
    ema_decision_number_of_paediatric_investigation_plan = Field()

    # Sponsor information (Section B)

    sponsors = Field(type=JSON)

    # Applicant Identification (Section C)

    # ...

    # IMP Identification (Section D)
    # IMP - investigated medicine product like drug

    imps = Field(type=JSON)

    # Information on Placebo (Section D8)

    placebos = Field(type=JSON)

    # General Information on the Trial (Section E)

    trial_medical_condition_s_being_investigated = Field()
    trial_medical_condition_in_easily_understood_language = Field()
    trial_therapeutic_area = Field()
    trial_version = Field()
    trial_level = Field()
    trial_classification_code = Field()
    trial_term = Field()
    trial_system_organ_class = Field()
    trial_condition_being_studied_is_a_rare_disease = Field()
    trial_main_objective_of_the_trial = Field()
    trial_secondary_objectives_of_the_trial = Field()
    trial_trial_contains_a_sub_study = Field()
    trial_principal_inclusion_criteria = Field()
    trial_principal_exclusion_criteria = Field()
    trial_primary_end_points = Field()
    trial_timepoints_of_evaluation_of_this_end_point = Field()
    trial_secondary_end_points = Field()
    trial_timepoints_of_evaluation_of_this_end_point = Field()
    trial_diagnosis = Field()
    trial_prophylaxis = Field()
    trial_therapy = Field()
    trial_safety = Field()
    trial_efficacy = Field()
    trial_pharmacokinetic = Field()
    trial_pharmacodynamic = Field()
    trial_bioequivalence = Field()
    trial_dose_response = Field()
    trial_pharmacogenetic = Field()
    trial_pharmacogenomic = Field()
    trial_pharmacoeconomic = Field()
    trial_others = Field()
    trial_human_pharmacology_phase_i = Field()
    trial_first_administration_to_humans = Field()
    trial_bioequivalence_study = Field()
    trial_other = Field()
    trial_therapeutic_exploratory_phase_ii = Field()
    trial_therapeutic_confirmatory_phase_iii = Field()
    trial_therapeutic_use_phase_iv = Field()
    trial_controlled = Field()
    trial_randomised = Field()
    trial_open = Field()
    trial_single_blind = Field()
    trial_double_blind = Field()
    trial_parallel_group = Field()
    trial_cross_over = Field()
    trial_other = Field()
    trial_other_medicinal_products = Field()
    trial_placebo = Field()
    trial_other = Field()
    trial_number_of_treatment_arms_in_the_trial = Field()
    trial_the_trial_involves_single_site_in_the_member = Field()
    trial_the_trial_involves_multiple_sites_in_the_member = Field()
    trial_the_trial_involves_multiple_member_states = Field()
    trial_trial_being_conducted_both_within_and_outside_the = Field()
    trial_trial_being_conducted_completely_outside_of_the_eea = Field()
    trial_trial_has_a_data_monitoring_committee = Field()
    trial_definition_of_the_end_of_the_trial_and = Field()
    trial_in_the_member_state_concerned_years = Field()
    trial_in_the_member_state_concerned_months = Field()
    trial_in_the_member_state_concerned_days = Field()

    # Population of Trial Subjects (Section F)

    subject_trial_has_subjects_under_18 = Field()
    subject_in_utero = Field()
    subject_preterm_newborn_infants_up_to_gestational_age_37 = Field()
    subject_newborns_0_27_days = Field()
    subject_infants_and_toddlers_28_days_23_months = Field()
    subject_children_2_11years = Field()
    subject_adolescents_12_17_years = Field()
    subject_adults_18_64_years = Field()
    subject_number_of_subjects_for_this_age_range = Field()
    subject_elderly_65_years = Field()
    subject_number_of_subjects_for_this_age_range = Field()
    subject_female = Field()
    subject_male = Field()
    subject_healthy_volunteers = Field()
    subject_patients = Field()
    subject_specific_vulnerable_populations = Field()
    subject_women_of_childbearing_potential_not_using_contraception = Field()
    subject_women_of_child_bearing_potential_using_contraception = Field()
    subject_pregnant_women = Field()
    subject_nursing_women = Field()
    subject_emergency_situation = Field()
    subject_subjects_incapable_of_giving_consent_personally = Field()
    subject_others = Field()
    subject_in_the_member_state = Field()
    subject_plans_for_treatment_or_care_after_the_subject = Field()

    # Investigator Networks to be involved in the Trial (Section G)

    # pass

    # Review by the Competent Authority or Ethics Committee (Section N)

    competent_authority_decision = Field()
    date_of_competent_authority_decision = Field()
    ethics_committee_opinion_of_the_trial_application = Field()
    ethics_committee_opinion_reasons_for_unfavourable_opinion = Field()
    date_of_ethics_committee_opinion = Field()

    # End of Trial (Section P)

    end_of_trial_status = Field()
