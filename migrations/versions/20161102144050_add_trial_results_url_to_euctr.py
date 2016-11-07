# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f35805a0a00f'
down_revision = u'84910d455f31'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('euctr', sa.Column('trial_results_url', sa.Text))


def downgrade():
    op.drop_column('euctr', 'trial_results_url')
