# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = 'ec1ab5776710'
down_revision = u'46d169ce43d2'
branch_labels = None
depends_on = None
tables = ['actrn', 'euctr', 'gsk', 'ictrp', 'isrctn', 'jprn', 'nct', 'pfizer', 'takeda']


def upgrade():
    for table in tables:
        op.rename_table(table, 'data_'+table)


def downgrade():
    for table in tables:
        op.rename_table('data_'+table, table)
