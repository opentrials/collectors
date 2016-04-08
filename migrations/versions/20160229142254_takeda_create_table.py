# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '393d51424903'
down_revision = u'a8d6e250d481'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('takeda',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('official_title', sa.Text),
        sa.Column('takeda_trial_id', sa.Text),
        sa.Column('trial_phase', sa.Text),
        sa.Column('condition', sa.Text),
        sa.Column('compound', ARRAY(sa.Text)),
        sa.Column('recruitment_status', sa.Text),

        # Description

        sa.Column('nct_number', sa.Text),
        sa.Column('trial_type', sa.Text),
        sa.Column('other_trial_ids', sa.Text),
        sa.Column('acronym', sa.Text),
        sa.Column('brief_summary', sa.Text),
        sa.Column('detailed_description', sa.Text),
        sa.Column('trial_design', sa.Text),
        sa.Column('primary_outcome_measures', sa.Text),
        sa.Column('secondary_outcome_measures', sa.Text),
        sa.Column('trial_armsgroups_or_cohorts', sa.Text),

        # Recruitment

        sa.Column('gender', sa.Text),
        sa.Column('ages', sa.Text),
        sa.Column('enrollmentnumber_of_participants', sa.Integer),
        sa.Column('locations', ARRAY(sa.Text)),
        sa.Column('responsible_party', sa.Text),
        sa.Column('trial_sponsor', sa.Text),
        sa.Column('start_date', sa.Date),
        sa.Column('completion_date', sa.Date),
        sa.Column('eligibility_criteria', sa.Text),

        # Results

        sa.Column('download_the_clinical_trial_summary', sa.Text),
        sa.Column('other_available_languages', sa.Text),

    )

def downgrade():
    op.drop_table('takeda')
