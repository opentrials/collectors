# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean, Integer, Json


# Module API

class Record(base.Record):

    # Config

    table = 'euctr'

    # Summary

    eudract_number_with_country = Text(primary_key=True)
    other_identifiers = Text()
    national_competent_authority = Text()
    clinical_trial_type = Text()
    trial_status = Text()
    date_on_which_this_record_was_first_entered_in_the_eudract_data = Date('%Y-%m-%d')
    trial_results = Text()
    trial_results_url = Text()

    # A. Protocol Information

    member_state_concerned = Text()
    eudract_number = Text()
    full_title_of_the_trial = Text()
    title_of_the_trial_for_lay_people_in_easily_understood_i_e_non_ = Text()
    name_or_abbreviated_title_of_the_trial_where_available = Text()
    sponsor_s_protocol_code_number = Text()
    us_nct_clinicaltrials_gov_registry_number = Text()
    who_universal_trial_reference_number_utrn = Text()
    isrctn_international_standard_randomised_controlled_trial_numbe = Text()
    trial_is_part_of_a_paediatric_investigation_plan = Boolean('Yes')
    ema_decision_number_of_paediatric_investigation_plan = Text()

    # B. Sponsor information

    sponsors = Json()

    # C. Applicant Identification

    # ...

    # D. IMP Identification

    imps = Json()

    # D8. Information on Placebo

    placebos = Json()

    # E. General Information on the Trial

    # E.1 Medical condition or disease under investigation
    trial_medical_condition_s_being_investigated = Text()
    trial_medical_condition_in_easily_understood_language = Text()
    trial_therapeutic_area = Text()
    trial_version = Text()
    trial_level = Text()
    trial_classification_code = Text()
    trial_term = Text()
    trial_system_organ_class = Text()
    trial_condition_being_studied_is_a_rare_disease = Text()

    # E.2 Objective of the trial
    trial_main_objective_of_the_trial = Text()
    trial_secondary_objectives_of_the_trial = Text()
    trial_trial_contains_a_sub_study = Boolean('Yes')
    trial_full_title_date_and_version_of_each_sub_study_and_their_r = Text()

    # E.3 and E.4 Eligibility
    trial_principal_inclusion_criteria = Text()
    trial_principal_exclusion_criteria = Text()

    # E.5 End points
    trial_primary_end_point_s = Text()
    trial_timepoint_s_of_evaluation_of_this_end_point = Text()
    trial_secondary_end_point_s = Text()
    trial_timepoint_s_of_evaluation_of_this_end_point = Text()

    # E.6 and E.7 Scope of the trial
    trial_diagnosis = Boolean('Yes')
    trial_prophylaxis = Boolean('Yes')
    trial_therapy = Boolean('Yes')
    trial_safety = Boolean('Yes')
    trial_efficacy = Boolean('Yes')
    trial_pharmacokinetic = Boolean('Yes')
    trial_pharmacodynamic = Boolean('Yes')
    trial_bioequivalence = Boolean('Yes')
    trial_dose_response = Boolean('Yes')
    trial_pharmacogenetic = Boolean('Yes')
    trial_pharmacogenomic = Boolean('Yes')
    trial_pharmacoeconomic = Boolean('Yes')
    trial_others = Boolean('Yes')
    trial_other_scope_of_the_trial_description = Text()
    trial_human_pharmacology_phase_i = Boolean('Yes')
    trial_first_administration_to_humans = Boolean('Yes')
    trial_bioequivalence_study = Boolean('Yes')
    trial_other_trial_type_description = Text()
    trial_other = Boolean('Yes')
    trial_therapeutic_exploratory_phase_ii = Boolean('Yes')
    trial_therapeutic_confirmatory_phase_iii = Boolean('Yes')
    trial_therapeutic_use_phase_iv = Boolean('Yes')

    # E.8 Design of the trial
    trial_controlled = Boolean('Yes')
    trial_randomised = Boolean('Yes')
    trial_open = Boolean('Yes')
    trial_single_blind = Boolean('Yes')
    trial_double_blind = Boolean('Yes')
    trial_parallel_group = Boolean('Yes')
    trial_cross_over = Boolean('Yes')
    trial_other_trial_design_description = Text()
    trial_other_medicinal_product_s = Boolean('Yes')
    trial_placebo = Boolean('Yes')
    trial_comparator_description = Text()
    trial_number_of_treatment_arms_in_the_trial = Integer()
    trial_the_trial_involves_single_site_in_the_member_state_concer = Boolean('Yes')
    trial_the_trial_involves_multiple_sites_in_the_member_state_con = Boolean('Yes')
    trial_number_of_sites_anticipated_in_member_state_concerned = Integer()
    trial_the_trial_involves_multiple_member_states = Boolean('Yes')
    trial_number_of_sites_anticipated_in_the_eea = Integer()

    # E.8.6 Trial involving sites outside the EEA
    trial_trial_being_conducted_both_within_and_outside_the_eea = Boolean('Yes')
    trial_trial_being_conducted_completely_outside_of_the_eea = Boolean('Yes')
    trial_specify_the_countries_outside_of_the_eea_in_which_trial_s = Text()
    trial_if_e_8_6_1_or_e_8_6_2_are_yes_specify_the_regions_in_whic = Text()
    trial_trial_has_a_data_monitoring_committee = Boolean('Yes')
    trial_definition_of_the_end_of_the_trial_and_justification_wher = Text()

    # E.8.9 Initial estimate of the duration of the trial
    trial_in_the_member_state_concerned_years = Integer()
    trial_in_the_member_state_concerned_months = Integer()
    trial_in_the_member_state_concerned_days = Integer()
    trial_in_all_countries_concerned_by_the_trial_years = Integer()
    trial_in_all_countries_concerned_by_the_trial_months = Integer()
    trial_in_all_countries_concerned_by_the_trial_days = Integer()

    # F. Population of Trial Subjects

    # F.1 Age Range
    subject_childs = Integer()
    subject_adults = Integer()
    subject_elderly = Integer()

    # F.2 Gender
    subject_female = Boolean('Yes')
    subject_male = Boolean('Yes')

    # F.3 Group of trial subjects
    subject_healthy_volunteers = Boolean('Yes')
    subject_patients = Boolean('Yes')
    subject_specific_vulnerable_populations = Boolean('Yes')
    subject_women_of_childbearing_potential_not_using_contraception = Boolean('Yes')
    subject_women_of_childbearing_potential_using_contraception = Boolean('Yes')
    subject_pregnant_women = Boolean('Yes')
    subject_nursing_women = Boolean('Yes')
    subject_emergency_situation = Boolean('Yes')
    subject_subjects_incapable_of_giving_consent_personally = Boolean('Yes')
    subject_details_of_subjects_incapable_of_giving_consent = Text()
    subject_others = Boolean('Yes')
    subject_details_of_other_specific_vulnerable_populations = Boolean('Yes')

    # F.4 Planned number of subjects to be included
    subject_in_the_member_state = Integer()
    subject_in_the_eea = Integer()
    subject_in_the_whole_clinical_trial = Integer()
    subject_plans_for_treatment_or_care_after_the_subject_has_ended = Text()

    # G. Investigator Networks to be involved in the Trial

    # pass

    # N. Review by the Competent Authority or Ethics Committee

    competent_authority_decision = Text()
    date_of_competent_authority_decision = Date('%Y-%m-%d')
    ethics_committee_opinion_of_the_trial_application = Text()
    ethics_committee_opinion_reason_s_for_unfavourable_opinion = Text()
    date_of_ethics_committee_opinion = Date('%Y-%m-%d')

    # P. End of Trial

    end_of_trial_status = Text()
    date_of_the_global_end_of_the_trial = Date('%Y-%m-%d')
