# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from alembic import op



# revision identifiers, used by Alembic.
revision = '46d169ce43d2'
down_revision = u'b0f8a397edad'
branch_labels = None
depends_on = None
tables = ['actrn', 'euctr', 'gsk', 'ictrp', 'isrctn', 'jprn', 'nct', 'pfizer', 'takeda']


def upgrade():
    for table in tables:
        op.alter_column(table, 'meta_uuid', new_column_name='meta_id')
        op.execute('ALTER TABLE %s ALTER COLUMN meta_id TYPE uuid USING meta_id::uuid' % table)


def downgrade():
    for table in tables:
        op.execute('ALTER TABLE %s ALTER COLUMN meta_id TYPE text USING meta_id::text' % table)
        op.alter_column(table, 'meta_id', new_column_name='meta_uuid')
