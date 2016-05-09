# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
from alembic import op


# revision identifiers, used by Alembic.
revision = 'be9dfe290c44'
down_revision = u'b720671a8c0f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('icdcm',

        # Meta

        sa.Column('meta_id', sa.Text, unique=True),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('name', sa.Text, primary_key=True),
        sa.Column('desc', sa.Text),
        sa.Column('terms', ARRAY(sa.Text)),
        sa.Column('version', sa.Text),
        sa.Column('last_updated', sa.Date),

    )


def downgrade():
    op.drop_table('icdcm')
