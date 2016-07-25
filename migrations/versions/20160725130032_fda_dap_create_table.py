# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '23c55ccc0649'
down_revision = u'3a3b663824f1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('fda_dap',

        # Meta

        sa.Column('meta_id', sa.Text, unique=True),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('id', sa.Text, unique=True),
        sa.Column('documents', JSONB),
        sa.Column('approval_type', sa.Text),
        sa.Column('supplement_number', sa.Integer),
        sa.Column('action_date', sa.Date),
        sa.Column('fda_application_num', sa.Text),
        sa.Column('notes', sa.Text),

    )


def downgrade():
    op.drop_table('fda_dap')
