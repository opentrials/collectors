# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = '6d709931cc58'
down_revision = u'c83c754cc04e'
branch_labels = None
depends_on = None

MAPPING = {
    'ethics_committee_opinion_reason_s_for_unfavourable_opinion': 'ethics_committee_opinion_reasons_for_unfavourable_opinion',
}


def upgrade():
    for key, value in MAPPING.items():
        op.alter_column('euctr', column_name=value, new_column_name=key)


def downgrade():
    for key, value in MAPPING.items():
        op.alter_column('euctr', column_name=key, new_column_name=value)
