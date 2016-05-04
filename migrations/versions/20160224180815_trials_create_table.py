# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from alembic import op


# revision identifiers, used by Alembic.
revision = 'c2ae4513dd2b'
down_revision = u'9833dacb0b30'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('trials',
        sa.Column('uuid', UUID, primary_key=True),
        sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
        sa.Column('records', ARRAY(sa.Text), nullable=False, unique=True),
        sa.Column('nct_id', sa.Text, unique=True),
        sa.Column('euctr_id', sa.Text, unique=True),
        sa.Column('isrctn_id', sa.Text, unique=True),
        sa.Column('scientific_title', sa.Text, unique=True),
    )


def downgrade():
    op.drop_table('trials')
