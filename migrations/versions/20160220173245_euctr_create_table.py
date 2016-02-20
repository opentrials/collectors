# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op



# revision identifiers, used by Alembic.
revision = '3433d4d2a0d1'
down_revision = '999c8f33bc04'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('euctr',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # Summary

        sa.Column('eudract_number_with_country', sa.Text, primary_key=True),
        sa.Column('other_identifiers', sa.Text),
        sa.Column('national_competent_authority', sa.Text),
        sa.Column('clinical_trial_type', sa.Text),
        sa.Column('trial_status', sa.Text),
        sa.Column('date_on_which_this_record_was_first_entered', sa.Date),
        sa.Column('trial_results', sa.Text),

        # A. Protocol Information

        sa.Column('member_state_concerned', sa.Text),
        sa.Column('eudract_number', sa.Text),
        sa.Column('full_title_of_the_trial', sa.Text),
        sa.Column('title_of_the_trial_for_lay_people_in', sa.Text),
        sa.Column('name_or_abbreviated_title_of_the_trial_where', sa.Text),
        sa.Column('sponsors_protocol_code_number', sa.Text),
        sa.Column('us_nct_clinicaltrialsgov_registry_number', sa.Text),
        sa.Column('who_universal_trial_reference_number_utrn', sa.Text),
        sa.Column('isrctn_international_standard_randomised_controlled_trial_number', sa.Text),
        sa.Column('trial_is_part_of_a_paediatric_investigation_plan', sa.Boolean),
        sa.Column('ema_decision_number_of_paediatric_investigation_plan', sa.Text),

        # B. Sponsor information

        sa.Column('sponsors', JSONB),

        # C. Applicant Identification

        # ...

        # D. IMP Identification

        sa.Column('imps', JSONB),

        # D8. Information on Placebo

        sa.Column('placebos', JSONB),

        # E. General Information on the Trial

        # E.1 Medical condition or disease under investigation
        sa.Column('trial_medical_conditions_being_investigated', sa.Text),
        sa.Column('trial_medical_condition_in_easily_understood_language', sa.Text),
        sa.Column('trial_therapeutic_area', sa.Text),
        sa.Column('trial_version', sa.Text),
        sa.Column('trial_level', sa.Text),
        sa.Column('trial_classification_code', sa.Text),
        sa.Column('trial_term', sa.Text),
        sa.Column('trial_system_organ_class', sa.Text),
        sa.Column('trial_condition_being_studied_is_a_rare_disease', sa.Text),

        # E.2 Objective of the trial
        sa.Column('trial_main_objective_of_the_trial', sa.Text),
        sa.Column('trial_secondary_objectives_of_the_trial', sa.Text),
        sa.Column('trial_trial_contains_a_substudy', sa.Boolean),
        sa.Column('trial_full_title_date_and_version_of_each_substudy', sa.Text),

        # E.3 and E.4 Eligibility
        sa.Column('trial_principal_inclusion_criteria', sa.Text),
        sa.Column('trial_principal_exclusion_criteria', sa.Text),

        # E.5 End points
        sa.Column('trial_primary_end_points', sa.Text),
        sa.Column('trial_timepoints_of_evaluation_of_this_end_point', sa.Text),
        sa.Column('trial_secondary_end_points', sa.Text),
        sa.Column('trial_timepoints_of_evaluation_of_this_end_point', sa.Text),

        # E.6 and E.7 Scope of the trial
        sa.Column('trial_diagnosis', sa.Boolean),
        sa.Column('trial_prophylaxis', sa.Boolean),
        sa.Column('trial_therapy', sa.Boolean),
        sa.Column('trial_safety', sa.Boolean),
        sa.Column('trial_efficacy', sa.Boolean),
        sa.Column('trial_pharmacokinetic', sa.Boolean),
        sa.Column('trial_pharmacodynamic', sa.Boolean),
        sa.Column('trial_bioequivalence', sa.Boolean),
        sa.Column('trial_dose_response', sa.Boolean),
        sa.Column('trial_pharmacogenetic', sa.Boolean),
        sa.Column('trial_pharmacogenomic', sa.Boolean),
        sa.Column('trial_pharmacoeconomic', sa.Boolean),
        sa.Column('trial_others', sa.Boolean),
        sa.Column('trial_other_scope_of_the_trial_description', sa.Text),
        sa.Column('trial_human_pharmacology_phase_i', sa.Boolean),
        sa.Column('trial_first_administration_to_humans', sa.Boolean),
        sa.Column('trial_bioequivalence_study', sa.Boolean),
        sa.Column('trial_other_trial_type_description', sa.Text),
        sa.Column('trial_other', sa.Boolean),
        sa.Column('trial_therapeutic_exploratory_phase_ii', sa.Boolean),
        sa.Column('trial_therapeutic_confirmatory_phase_iii', sa.Boolean),
        sa.Column('trial_therapeutic_use_phase_iv', sa.Boolean),

        # E.8 Design of the trial
        sa.Column('trial_controlled', sa.Boolean),
        sa.Column('trial_randomised', sa.Boolean),
        sa.Column('trial_open', sa.Boolean),
        sa.Column('trial_single_blind', sa.Boolean),
        sa.Column('trial_double_blind', sa.Boolean),
        sa.Column('trial_parallel_group', sa.Boolean),
        sa.Column('trial_cross_over', sa.Boolean),
        sa.Column('trial_other_trial_design_description', sa.Text),
        sa.Column('trial_other_medicinal_products', sa.Boolean),
        sa.Column('trial_placebo', sa.Boolean),
        sa.Column('trial_comparator_description', sa.Text),
        sa.Column('trial_number_of_treatment_arms_in_the_trial', sa.Integer),
        sa.Column('trial_the_trial_involves_single_site_in_the_member', sa.Boolean),
        sa.Column('trial_the_trial_involves_multiple_sites_in_the_member', sa.Boolean),
        sa.Column('trial_number_of_sites_anticipated_in_member_state_concerned', sa.Integer),
        sa.Column('trial_the_trial_involves_multiple_member_states', sa.Boolean),
        sa.Column('trial_number_of_sites_anticipated_in_the_eea', sa.Integer),

        # E.8.6 Trial involving sites outside the EEA
        sa.Column('trial_trial_being_conducted_both_within_and_outside_the', sa.Boolean),
        sa.Column('trial_trial_being_conducted_completely_outside_of_the_eea', sa.Boolean),
        sa.Column('trial_specify_the_countries_outside_of_the_eea_in', sa.Text),
        sa.Column('trial_if_e861_or_e862_are_yes_specify_the', sa.Text),
        sa.Column('trial_trial_has_a_data_monitoring_committee', sa.Boolean),
        sa.Column('trial_definition_of_the_end_of_the_trial_and', sa.Text),

        # E.8.9 Initial estimate of the duration of the trial
        sa.Column('trial_in_the_member_state_concerned_years', sa.Integer),
        sa.Column('trial_in_the_member_state_concerned_months', sa.Integer),
        sa.Column('trial_in_the_member_state_concerned_days', sa.Integer),
        sa.Column('trial_in_all_countries_concerned_by_the_trial_years', sa.Integer),
        sa.Column('trial_in_all_countries_concerned_by_the_trial_months', sa.Integer),
        sa.Column('trial_in_all_countries_concerned_by_the_trial_days', sa.Integer),

        # F. Population of Trial Subjects

        # F.1 Age Range
        sa.Column('subject_childs', sa.Integer),
        sa.Column('subject_adults', sa.Integer),
        sa.Column('subject_elderly', sa.Integer),

        # F.2 Gender
        sa.Column('subject_female', sa.Boolean),
        sa.Column('subject_male', sa.Boolean),

        # F.3 Group of trial subjects
        sa.Column('subject_healthy_volunteers', sa.Boolean),
        sa.Column('subject_patients', sa.Boolean),
        sa.Column('subject_specific_vulnerable_populations', sa.Boolean),
        sa.Column('subject_women_of_childbearing_potential_not_using_contraception', sa.Boolean),  # noqa
        sa.Column('subject_women_of_childbearing_potential_using_contraception', sa.Boolean),  # noqa
        sa.Column('subject_pregnant_women', sa.Boolean),
        sa.Column('subject_nursing_women', sa.Boolean),
        sa.Column('subject_emergency_situation', sa.Boolean),
        sa.Column('subject_subjects_incapable_of_giving_consent_personally', sa.Boolean),
        sa.Column('subject_details_of_subjects_incapable_of_giving_consent', sa.Text),
        sa.Column('subject_others', sa.Boolean),
        sa.Column('subject_details_of_other_specific_vulnerable_populations', sa.Boolean),

        # F.4 Planned number of subjects to be included
        sa.Column('subject_in_the_member_state', sa.Integer),
        sa.Column('subject_in_the_eea', sa.Integer),
        sa.Column('subject_in_the_whole_clinical_trial', sa.Integer),
        sa.Column('subject_plans_for_treatment_or_care_after_the_subject', sa.Text),

        # G. Investigator Networks to be involved in the Trial

        # pass

        # N. Review by the Competent Authority or Ethics Committee

        sa.Column('competent_authority_decision', sa.Text),
        sa.Column('date_of_competent_authority_decision', sa.Date),
        sa.Column('ethics_committee_opinion_of_the_trial_application', sa.Text),
        sa.Column('ethics_committee_opinion_reasons_for_unfavourable_opinion', sa.Text),
        sa.Column('date_of_ethics_committee_opinion', sa.Date),

        # P. End of Trial

        sa.Column('end_of_trial_status', sa.Text),
        sa.Column('date_of_the_global_end_of_the_trial', sa.Date),

    )


def downgrade():
    pass
