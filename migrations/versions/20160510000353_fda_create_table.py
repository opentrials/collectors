# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '9f367826f849'
down_revision = u'6a990542e4b4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('fda',

        # Meta

        sa.Column('meta_id', sa.Text, unique=True),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('product_ndc', sa.Text, primary_key=True),
        sa.Column('product_type', sa.Text),
        sa.Column('generic_name', sa.Text),
        sa.Column('brand_name', sa.Text),
        sa.Column('last_updated', sa.Date),

    )


def downgrade():
    op.drop_table('fda')
