# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d52470f8e49'
down_revision = u'bc7470719f51'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('fda_dap') as batch_op:
        batch_op.add_column(sa.Column('drug_name', sa.Text))
        batch_op.add_column(sa.Column('active_ingredients', sa.Text))
        batch_op.add_column(sa.Column('company', sa.Text))


def downgrade():
    with op.batch_alter_table('fda_dap') as batch_op:
        batch_op.drop_column('drug_name')
        batch_op.drop_column('active_ingredients')
        batch_op.drop_column('company')
