# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = 'babb1b77ca56'
down_revision = u'296d1e273220'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('actrn',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('trial_id', sa.Text, primary_key=True),
        sa.Column('ethics_application_status', sa.Text),
        sa.Column('date_submitted', sa.Date),
        sa.Column('date_registered', sa.Date),
        sa.Column('type_of_registration', sa.Text),

        # Titles & IDs

        sa.Column('public_title', sa.Text),
        sa.Column('scientific_title', sa.Text),
        sa.Column('secondary_ids', ARRAY(sa.Text)),
        sa.Column('universal_trial_number_utn', sa.Text),
        sa.Column('trial_acronym', sa.Text),

        # Health condition

        sa.Column('health_conditions_or_problems_studied', sa.Text),
        sa.Column('condition_category', sa.Text),
        sa.Column('condition_code', sa.Text),

        # Intervention/exposure

        sa.Column('study_type', sa.Text),
        sa.Column('patient_registry', sa.Boolean),
        sa.Column('target_followup_duration', sa.Integer),
        sa.Column('target_followup_type', sa.Text),
        sa.Column('description_of_interventions__exposure', sa.Text),
        sa.Column('intervention_codes', ARRAY(sa.Text)),
        sa.Column('comparator__control_treatment', sa.Text),
        sa.Column('control_group', sa.Text),

        # Outcomes

        sa.Column('primary_outcomes', JSONB),
        sa.Column('secondary_outcomes', JSONB),

        # Eligibility

        sa.Column('key_inclusion_criteria', sa.Text),
        sa.Column('minimum_age', sa.Text),
        sa.Column('maximum_age', sa.Text),
        sa.Column('gender', sa.Text),
        sa.Column('can_healthy_volunteers_participate', sa.Boolean),
        sa.Column('key_exclusion_criteria', sa.Text),

        # Study design

        sa.Column('purpose_of_the_study', sa.Text),
        sa.Column('allocation_to_intervention', sa.Text),
        sa.Column('procedure_for_enrolling_a_subject_and_allocating_the', sa.Text),
        sa.Column('methods_used_to_generate_the_sequence_in_which', sa.Text),
        sa.Column('masking__blinding', sa.Text),
        sa.Column('who_is__are_masked__blinded', sa.Text),
        sa.Column('intervention_assignment', sa.Text),
        sa.Column('other_design_features', sa.Text),
        sa.Column('phase', sa.Text),
        sa.Column('type_of_endpoints', sa.Text),
        sa.Column('purpose', sa.Text),
        sa.Column('duration', sa.Text),
        sa.Column('selection', sa.Text),
        sa.Column('timing', sa.Text),
        sa.Column('statistical_methods__analysis', sa.Text),

        # Recruitment

        sa.Column('anticipated_date_of_first_participant_enrolment', sa.Date),
        sa.Column('actual_date_of_first_participant_enrolment', sa.Date),
        sa.Column('anticipated_date_last_participant_enrolled', sa.Date),
        sa.Column('actual_date_last_participant_enrolled', sa.Date),
        sa.Column('target_sample_size', sa.Integer),
        sa.Column('actual_sample_size', sa.Integer),
        sa.Column('recruitment_status', sa.Text),
        sa.Column('recruitment_states', sa.Text),

        # Funding & Sponsors

        sa.Column('primary_sponsor', JSONB),
        sa.Column('sponsors', JSONB),

        # Ethics approval

        sa.Column('ethics_application_status', sa.Text),
        sa.Column('ethics_applications', JSONB),

        # Summary

        sa.Column('brief_summary', sa.Text),
        sa.Column('trial_website', sa.Text),
        sa.Column('trial_related_presentations__publications', sa.Text),
        sa.Column('public_notes', sa.Text),
        sa.Column('attachments', ARRAY(sa.Text)),

        # Contacts

        sa.Column('principal_investigator', JSONB),
        sa.Column('public_queries', JSONB),
        sa.Column('scientific_queries', JSONB),

    )


def downgrade():
    op.drop_table('actrn')
