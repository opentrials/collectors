# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '999c8f33bc04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('nct',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('download_date', sa.Text),
        sa.Column('link_text', sa.Text),
        sa.Column('url', sa.Text),
        sa.Column('org_study_id', sa.Text),
        sa.Column('nct_id', sa.Text, primary_key=True),
        sa.Column('secondary_ids', ARRAY(sa.Text)),
        sa.Column('nct_aliases', ARRAY(sa.Text)),
        sa.Column('brief_title', sa.Text),
        sa.Column('acronym', sa.Text),
        sa.Column('official_title', sa.Text),
        sa.Column('sponsors', JSONB),
        sa.Column('source', sa.Text),
        sa.Column('oversight_info', JSONB),
        sa.Column('brief_summary', sa.Text),
        sa.Column('detailed_description', sa.Text),
        sa.Column('overall_status', sa.Text),
        sa.Column('why_stopped', sa.Text),
        sa.Column('start_date', sa.Date),
        sa.Column('completion_date_actual', sa.Date),
        sa.Column('completion_date_anticipated', sa.Date),
        sa.Column('primary_completion_date_actual', sa.Date),
        sa.Column('primary_completion_date_anticipated', sa.Date),
        sa.Column('phase', sa.Text),
        sa.Column('study_type', sa.Text),
        sa.Column('study_design', sa.Text),
        sa.Column('target_duration', sa.Text),
        sa.Column('primary_outcomes', JSONB),
        sa.Column('secondary_outcomes', JSONB),
        sa.Column('other_outcomes', JSONB),
        sa.Column('number_of_arms', sa.Integer),
        sa.Column('number_of_groups', sa.Integer),
        sa.Column('enrollment_actual', sa.Integer),
        sa.Column('enrollment_anticipated', sa.Integer),
        sa.Column('conditions', ARRAY(sa.Text)),
        sa.Column('arm_groups', JSONB),
        sa.Column('interventions', JSONB),
        sa.Column('biospec_retention', sa.Text),
        sa.Column('biospec_desrc', sa.Text),
        sa.Column('eligibility', JSONB),
        sa.Column('overall_officials', JSONB),
        sa.Column('overall_contact', JSONB),
        sa.Column('overall_contact_backup', JSONB),
        sa.Column('locations', JSONB),
        sa.Column('location_countries', ARRAY(sa.Text)),
        sa.Column('removed_countries', ARRAY(sa.Text)),
        sa.Column('links', JSONB),
        sa.Column('references', JSONB),
        sa.Column('results_references', JSONB),
        sa.Column('verification_date', sa.Date),
        sa.Column('lastchanged_date', sa.Date),
        sa.Column('firstreceived_date', sa.Date),
        sa.Column('firstreceived_results_date', sa.Date),
        sa.Column('responsible_party', JSONB),
        sa.Column('keywords', ARRAY(sa.Text)),
        sa.Column('is_fda_regulated', sa.Text),
        sa.Column('is_section_801', sa.Text),
        sa.Column('has_expanded_access', sa.Text),
        sa.Column('condition_browse', JSONB),
        sa.Column('intervention_browse', JSONB),
        sa.Column('clinical_results', JSONB),

    )


def downgrade():
    pass
