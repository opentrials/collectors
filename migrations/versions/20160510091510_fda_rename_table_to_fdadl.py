# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = 'f38e14eac095'
down_revision = u'9f367826f849'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('fda', 'fdadl')


def downgrade():
    op.rename_table('fdadl', 'fda')
