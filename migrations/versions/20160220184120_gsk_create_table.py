# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '820db6031f39'
down_revision = u'33a5e999fd54'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('gsk',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('study_id', sa.Text, primary_key=True),
        sa.Column('study_title', sa.Text),
        sa.Column('patient_level_data', sa.Text),
        sa.Column('clinicaltrialsgov_identifier', sa.Text),
        sa.Column('sponsor', sa.Text),
        sa.Column('collaborators', sa.Text),
        sa.Column('study_recruitment_status', sa.Text),
        sa.Column('generic_name', sa.Text),
        sa.Column('trade_name', sa.Text),
        sa.Column('study_indication', sa.Text),

        # Protocol summary

        sa.Column('first_received', sa.Date),
        sa.Column('last_updated', sa.Date),
        sa.Column('title', sa.Text),
        sa.Column('phase', sa.Text),
        sa.Column('acronym', sa.Text),
        sa.Column('secondary_ids', ARRAY(sa.Text)),
        sa.Column('fda_regulated_intervention', sa.Boolean),
        sa.Column('section_801_clinical_trial', sa.Boolean),
        sa.Column('delayed_posting', sa.Boolean),
        sa.Column('indide_protocol', sa.Text),
        sa.Column('indide_grantor', sa.Text),
        sa.Column('indide_number', sa.Text),
        sa.Column('indide_serial_number', sa.Text),
        sa.Column('has_expanded_access', sa.Boolean),
        sa.Column('study_type', sa.Text),
        sa.Column('oversight_authority', ARRAY(sa.Text)),
        sa.Column('sponsor', sa.Text),
        sa.Column('collaborators', ARRAY(sa.Text)),
        sa.Column('brief_summary', sa.Text),
        sa.Column('detailed_description', sa.Text),
        sa.Column('record_verification_date', sa.Date),
        sa.Column('status', sa.Text),
        sa.Column('why_study_stopped', sa.Text),
        sa.Column('study_start_date', sa.Date),
        sa.Column('study_completion_date', sa.Date),
        sa.Column('study_completion_date_type', sa.Text),
        sa.Column('primary_completion_date', sa.Date),
        sa.Column('primary_completion_date_type', sa.Text),
        sa.Column('primary_purpose', sa.Text),
        sa.Column('study_design', sa.Text),
        sa.Column('time_perspective', sa.Text),
        sa.Column('biospecimen_retention', sa.Text),
        sa.Column('biospecimen_description', sa.Text),
        sa.Column('allocation', sa.Text),
        sa.Column('masking', sa.Text),
        sa.Column('masked_subject', sa.Boolean),
        sa.Column('masked_caregiver', sa.Boolean),
        sa.Column('masked_investigator', sa.Boolean),
        sa.Column('masked_assessor', sa.Boolean),
        sa.Column('study_design_assignment', sa.Text),
        sa.Column('study_classification_endpoint', sa.Text),
        sa.Column('primary_outcomes', JSONB),
        sa.Column('secondary_outcomes', JSONB),
        sa.Column('arms', JSONB),
        sa.Column('interventions', JSONB),
        sa.Column('conditions', ARRAY(sa.Text)),
        sa.Column('keywords', ARRAY(sa.Text)),
        sa.Column('study_population', sa.Text),
        sa.Column('sampling_method', sa.Text),
        sa.Column('eligibility_criteria', sa.Text),
        sa.Column('gender', sa.Text),
        sa.Column('minimum_age', sa.Text),
        sa.Column('maximum_age', sa.Text),
        sa.Column('enrollment', sa.Integer),
        sa.Column('enrollment_type', sa.Text),
        sa.Column('healthy_volunteers', sa.Boolean),
        sa.Column('central_contact', sa.Text),
        sa.Column('central_contact_phone', sa.Text),
        sa.Column('central_contact_email', sa.Text),
        sa.Column('overall_study_official', sa.Text),
        sa.Column('overall_study_official_affiliation', sa.Text),
        sa.Column('overall_study_official_role', sa.Text),
        sa.Column('responsible_party_nameofficial_title', sa.Text),
        sa.Column('responsible_party_organization', sa.Text),

        # Locations

        sa.Column('contact_name', sa.Text),
        sa.Column('contact_phone', sa.Text),
        sa.Column('contact_email', sa.Text),

        # Result summary

        sa.Column('protocol_id', sa.Text),
        sa.Column('clinical_study_id', sa.Text),
        sa.Column('official_study_title', sa.Text),
        sa.Column('phase', sa.Text),
        sa.Column('study_indication_or_diseases', sa.Text),
        sa.Column('generic_name', sa.Text),
        sa.Column('trade_name', sa.Text),
        sa.Column('trade_name__product_name', sa.Text),
        sa.Column('study_indications', sa.Text),

        # Publication

        sa.Column('citation', sa.Text),
        sa.Column('publication_type', sa.Text),

    )


def downgrade():
    op.drop_table('gsk')
