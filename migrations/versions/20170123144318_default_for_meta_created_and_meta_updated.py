# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542425c4e70b'
down_revision = u'0087dc1eb534'
branch_labels = None
depends_on = None

updatable_tables = ['actrn', 'cochrane_reviews', 'euctr', 'fda_dap', 'fdadl', 'gsk',
    'hra', 'icdcm', 'icdpcs', 'ictrp', 'isrctn', 'jprn', 'nct', 'pfizer', 'pubmed', 'takeda']


def upgrade():
    for table in updatable_tables:
        op.alter_column(table, 'meta_created', nullable=False,
                        server_default=sa.func.current_timestamp())
        op.alter_column(table, 'meta_updated', nullable=False,
                        server_default=sa.func.current_timestamp())


def downgrade():
    for table in updatable_tables:
        op.alter_column(table, 'meta_created', nullable=True, server_default=None)
        op.alter_column(table, 'meta_updated', nullable=True, server_default=None)
