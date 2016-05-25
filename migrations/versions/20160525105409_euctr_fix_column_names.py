# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = '11f80cc2fafb'
down_revision = u'f38e14eac095'
branch_labels = None
depends_on = None

MAPPING = {
    'date_on_which_this_record_was_first_entered_in_the_eudract_data': 'date_on_which_this_record_was_first_entered',
    'name_or_abbreviated_title_of_the_trial_where_available': 'name_or_abbreviated_title_of_the_trial_where',
    'sponsor_s_protocol_code_number': 'sponsors_protocol_code_number',
    'subject_plans_for_treatment_or_care_after_the_subject_has_ended': 'subject_plans_for_treatment_or_care_after_the_subject',
    'title_of_the_trial_for_lay_people_in_easily_understood_i_e_non_': 'title_of_the_trial_for_lay_people_in',
    'trial_definition_of_the_end_of_the_trial_and_justification_wher': 'trial_definition_of_the_end_of_the_trial_and',
    'trial_full_title_date_and_version_of_each_sub_study_and_their_r': 'trial_full_title_date_and_version_of_each_substudy',
    'trial_if_e_8_6_1_or_e_8_6_2_are_yes_specify_the_regions_in_whic': 'trial_if_e861_or_e862_are_yes_specify_the',
    'trial_medical_condition_s_being_investigated': 'trial_medical_conditions_being_investigated',
    'trial_other_medicinal_product_s': 'trial_other_medicinal_products',
    'trial_primary_end_point_s': 'trial_primary_end_points',
    'trial_secondary_end_point_s': 'trial_secondary_end_points',
    'trial_specify_the_countries_outside_of_the_eea_in_which_trial_s': 'trial_specify_the_countries_outside_of_the_eea_in',
    'trial_the_trial_involves_multiple_sites_in_the_member_state_con': 'trial_the_trial_involves_multiple_sites_in_the_member',
    'trial_the_trial_involves_single_site_in_the_member_state_concer': 'trial_the_trial_involves_single_site_in_the_member',
    'trial_timepoint_s_of_evaluation_of_this_end_point': 'trial_timepoints_of_evaluation_of_this_end_point',
    'trial_trial_being_conducted_both_within_and_outside_the_eea': 'trial_trial_being_conducted_both_within_and_outside_the',
    'trial_trial_contains_a_sub_study': 'trial_trial_contains_a_substudy',
    'us_nct_clinicaltrials_gov_registry_number': 'us_nct_clinicaltrialsgov_registry_number',
}


def upgrade():
    for key, value in MAPPING.items():
        op.alter_column('euctr', column_name=value, new_column_name=key)


def downgrade():
    for key, value in MAPPING.items():
        op.alter_column('euctr', column_name=key, new_column_name=value)
