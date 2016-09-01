# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf807df84277'
down_revision = u'2d52470f8e49'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('gsk', sa.Column('results_url', sa.Text))


def downgrade():
    op.drop_column('gsk', 'results_url')
