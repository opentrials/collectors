# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op



# revision identifiers, used by Alembic.
revision = '7518ba857fea'
down_revision = u'393d51424903'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('ictrp',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # Main

        sa.Column('register', sa.Text, primary_key=True),
        sa.Column('last_refreshed_on', sa.Date),
        sa.Column('main_id', sa.Text, primary_key=True),
        sa.Column('date_of_registration', sa.Text),
        sa.Column('primary_sponsor', sa.Text),
        sa.Column('public_title', sa.Text),
        sa.Column('scientific_title', sa.Text),
        sa.Column('date_of_first_enrollment', sa.Text),
        sa.Column('target_sample_size', sa.Integer),
        sa.Column('recruitment_status', sa.Text),
        sa.Column('url', sa.Text),
        sa.Column('study_type', sa.Text),
        sa.Column('study_design', sa.Text),
        sa.Column('study_phase', sa.Text),

        # Additional

        sa.Column('countries_of_recruitment', ARRAY(sa.Text)),
        sa.Column('contacts', JSONB),
        sa.Column('key_inclusion_exclusion_criteria', sa.Text),
        sa.Column('health_conditions_or_problems_studied', ARRAY(sa.Text)),
        sa.Column('interventions', ARRAY(sa.Text)),
        sa.Column('primary_outcomes', ARRAY(sa.Text)),
        sa.Column('secondary_outcomes', ARRAY(sa.Text)),
        sa.Column('secondary_ids', ARRAY(sa.Text)),
        sa.Column('sources_of_monetary_support', ARRAY(sa.Text)),
        sa.Column('secondary_sponsors', ARRAY(sa.Text)),

    )

def downgrade():
    op.drop_table('ictrp')
