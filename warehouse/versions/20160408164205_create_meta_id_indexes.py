# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '014fd3f703aa'
down_revision = u'00d329f5f40a'
branch_labels = None
depends_on = None
tables = ['actrn', 'euctr', 'gsk', 'ictrp', 'isrctn', 'jprn', 'nct', 'pfizer', 'takeda']


def upgrade():
    for table in tables:
        op.create_unique_constraint('%s_meta_id_unique' % table, table, ['meta_id'])


def downgrade():
    for table in tables:
        op.drop_constraint('%s_meta_id_unique' % table, table)
