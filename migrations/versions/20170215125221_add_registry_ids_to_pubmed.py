# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd0bb12971d2'
down_revision = u'3dbb46f23ed7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pubmed', sa.Column('registry_ids', sa.dialects.postgresql.JSONB))


def downgrade():
    op.drop_column('pubmed', 'registry_ids')
