# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = '3a3b663824f1'
down_revision = u'c4c0db99bb1c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pubmed', sa.Column('mesh_headings', JSONB))


def downgrade():
    op.drop_column('pubmed', 'mesh_headings')
