# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc7470719f51'
down_revision = u'23c55ccc0649'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('fdadl', sa.Column('fda_application_number', sa.Text))


def downgrade():
    op.drop_column('fdadl', 'fda_application_number')
