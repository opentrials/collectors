# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '84910d455f31'
down_revision = u'bf807df84277'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cochrane_reviews',
        sa.Column('meta_id', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('meta_updated', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('meta_source', sa.Text),

        sa.Column('id', UUID, primary_key=True),
        sa.Column('study_type', sa.Text),
        sa.Column('file_name', sa.Text),
        sa.Column('robs', JSONB),
        sa.Column('study_id', sa.Text),
        sa.Column('refs', JSONB),
        sa.Column('doi_id', sa.Text),
    )


def downgrade():
    op.drop_table('nct')
