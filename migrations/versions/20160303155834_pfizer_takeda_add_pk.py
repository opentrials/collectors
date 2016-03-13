# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b0f8a397edad'
down_revision = u'7518ba857fea'
branch_labels = None
depends_on = None


def upgrade():
    op.create_primary_key('pfizer_pkey', 'pfizer', ['nct_id'])
    op.create_primary_key('takeda_pkey', 'takeda', ['takeda_trial_id'])


def downgrade():
    op.drop_constraint('pfizer_pkey', 'pfizer')
    op.drop_constraint('takeda_pkey', 'takeda')
