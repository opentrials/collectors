# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = 'e77e7eaf0a34'
down_revision = u'11f80cc2fafb'
branch_labels = None
depends_on = None

MAPPING = {
    'type_of_endpoint_s': 'type_of_endpoints',
    'who_is_are_masked_blinded': 'who_is__are_masked__blinded',
    'masking_blinding': 'masking__blinding',
    'description_of_intervention_s_exposure': 'description_of_interventions__exposure',
    'comparator_control_treatment': 'comparator__control_treatment',
    'recruitment_state_s': 'recruitment_states',
    'procedure_for_enrolling_a_subject_and_allocating_the_treatment_': 'procedure_for_enrolling_a_subject_and_allocating_the',
    'methods_used_to_generate_the_sequence_in_which_subjects_will_be': 'methods_used_to_generate_the_sequence_in_which',
    'statistical_methods_analysis': 'statistical_methods__analysis',
    'trial_related_presentations_publications': 'trial_related_presentations__publications',
    'target_follow_up_duration': 'target_followup_duration',
    'target_follow_up_type': 'target_followup_type',
}


def upgrade():
    for key, value in MAPPING.items():
        op.alter_column('actrn', column_name=value, new_column_name=key)


def downgrade():
    for key, value in MAPPING.items():
        op.alter_column('actrn', column_name=key, new_column_name=value)
