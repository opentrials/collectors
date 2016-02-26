# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op



# revision identifiers, used by Alembic.
revision = 'a8d6e250d481'
down_revision = u'c2ae4513dd2b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('pfizer',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('title', sa.Text),

        # Description

        sa.Column('study_type', sa.Text),
        sa.Column('organization_id', sa.Text),
        sa.Column('nct_id', sa.Text),
        sa.Column('status', sa.Text),
        sa.Column('study_start_date', sa.Date),
        sa.Column('study_end_date', sa.Date),

        # Eligibility

        sa.Column('eligibility_criteria', sa.Text),
        sa.Column('gender', sa.Text),
        sa.Column('age_range', sa.Text),
        sa.Column('healthy_volunteers_allowed', sa.Boolean),

    )

def downgrade():
    op.drop_table('pfizer')
