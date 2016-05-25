# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = 'c83c754cc04e'
down_revision = u'59e2335b3d41'
branch_labels = None
depends_on = None

MAPPING = {
    'enrollment_number_of_participants': 'enrollmentnumber_of_participants',
    'trial_arms_groups_or_cohorts': 'trial_armsgroups_or_cohorts',
}


def upgrade():
    for key, value in MAPPING.items():
        op.alter_column('takeda', column_name=value, new_column_name=key)


def downgrade():
    for key, value in MAPPING.items():
        op.alter_column('takeda', column_name=key, new_column_name=value)
