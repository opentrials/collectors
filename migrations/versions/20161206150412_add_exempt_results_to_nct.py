# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0087dc1eb534'
down_revision = u'f35805a0a00f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('nct', sa.Column('results_exemption_date', sa.Date))


def downgrade():
    op.drop_column('nct', 'results_exemption_date')
