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
    us_nct_clinicaltrialsgov_registry_number = Field()
    national_competent_authority = Field()
    clinical_trial_type = Field()
    trial_status = Field()
    date_on_which_this_record_was_first_entered = Field(type=sa.Date)
    trial_results = Field()

    # A. Protocol Information

    member_state_concerned = Field()
    full_title_of_the_trial = Field()
    title_of_the_trial_for_lay_people_in = Field()
    name_or_abbreviated_title_of_the_trial_where = Field()
    sponsors_protocol_code_number = Field()
    isrctn_international_standard_randomised_controlled_trial_number = Field()
    trial_is_part_of_a_paediatric_investigation_plan = Field()
    ema_decision_number_of_paediatric_investigation_plan = Field()

    # B. Sponsor information

    sponsors = Field(type=JSON)

    # C. Applicant Identification

    # ...

    # D. IMP Identification

    imps = Field(type=JSON)

    # D8. Information on Placebo

    placebos = Field(type=JSON)

    # E. General Information on the Trial

    # E.1 Medical condition or disease under investigation
    trial_medical_conditions_being_investigated = Field()
    trial_medical_condition_in_easily_understood_language = Field()
    trial_therapeutic_area = Field()
    trial_version = Field()
    trial_level = Field()
    trial_classification_code = Field()
    trial_term = Field()
    trial_system_organ_class = Field()
    trial_condition_being_studied_is_a_rare_disease = Field()

    # E.2 Objective of the trial
    trial_main_objective_of_the_trial = Field()
    trial_secondary_objectives_of_the_trial = Field()
    trial_trial_contains_a_substudy = Field()
    trial_full_title_date_and_version_of_each_substudy = Field()

    # E.3 and E.4 Eligibility
    trial_principal_inclusion_criteria = Field()
    trial_principal_exclusion_criteria = Field()

    # E.5 End points
    trial_primary_end_points = Field()
    trial_timepoints_of_evaluation_of_this_end_point = Field()
    trial_secondary_end_points = Field()
    trial_timepoints_of_evaluation_of_this_end_point = Field()

    # E.6 and E.7 Scope of the trial
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

    # E.8 Design of the trial
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
    trial_comparator_description = Field()
    trial_number_of_treatment_arms_in_the_trial = Field()
    trial_the_trial_involves_single_site_in_the_member = Field()
    trial_the_trial_involves_multiple_sites_in_the_member = Field()
    trial_number_of_sites_anticipated_in_member_state_concerned = Field()
    trial_the_trial_involves_multiple_member_states = Field()
    trial_number_of_sites_anticipated_in_the_eea = Field()
    trial_trial_being_conducted_both_within_and_outside_the = Field()
    trial_trial_being_conducted_completely_outside_of_the_eea = Field()
    trial_if_e861_or_e862_are_yes_specify_the = Field()
    trial_trial_has_a_data_monitoring_committee = Field()
    trial_definition_of_the_end_of_the_trial_and = Field()

    # E.8.9 Initial estimate of the duration of the trial
    trial_in_the_member_state_concerned_years = Field()
    trial_in_the_member_state_concerned_months = Field()
    trial_in_the_member_state_concerned_days = Field()
    trial_in_all_countries_concerned_by_the_trial_years = Field()
    trial_in_all_countries_concerned_by_the_trial_months = Field()
    trial_in_all_countries_concerned_by_the_trial_days = Field()

    # F. Population of Trial Subjects

    # F.1 Age Range
    subject_trial_has_subjects_under_18 = Field()
    subject_in_utero = Field()
    subject_preterm_newborn_infants_up_to_gestational_age_ = Field()
    subject_newborns_027_days = Field()
    subject_infants_and_toddlers_28_days23_months = Field()
    subject_children_211years = Field()
    subject_adolescents_1217_years = Field()
    subject_adults_1864_years = Field()
    subject_elderly_65_years = Field()

    # F.2 Gender
    subject_female = Field()
    subject_male = Field()

    # F.3 Group of trial subjects
    subject_healthy_volunteers = Field()
    subject_patients = Field()
    subject_specific_vulnerable_populations = Field()
    subject_women_of_childbearing_potential_using_contraception = Field()
    subject_women_of_childbearing_potential_not_using_contraception = Field()
    subject_women_of_child_bearing_potential_using_contraception = Field()
    subject_pregnant_women = Field()
    subject_nursing_women = Field()
    subject_emergency_situation = Field()
    subject_subjects_incapable_of_giving_consent_personally = Field()
    subject_details_of_subjects_incapable_of_giving_consent = Field()
    subject_others = Field()

    # F.4 Planned number of subjects to be included
    subject_in_the_member_state = Field()
    subject_in_the_eea = Field()
    subject_in_the_whole_clinical_trial = Field()
    subject_plans_for_treatment_or_care_after_the_subject = Field()

    # G. Investigator Networks to be involved in the Trial

    # pass

    # N. Review by the Competent Authority or Ethics Committee

    competent_authority_decision = Field()
    date_of_competent_authority_decision = Field()
    ethics_committee_opinion_of_the_trial_application = Field()
    ethics_committee_opinion_reasons_for_unfavourable_opinion = Field()
    date_of_ethics_committee_opinion = Field()

    # P. End of Trial

    end_of_trial_status = Field()
