# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = '59e2335b3d41'
down_revision = u'f736bb9d2499'
branch_labels = None
depends_on = None

MAPPING = {
    'prospective_retrospective': 'prospectiveretrospective',
    'protocol_serial_number': 'protocolserial_number',
    'clinicaltrials_gov_number': 'clinicaltrialsgov_number',
}


def upgrade():
    for key, value in MAPPING.items():
        op.alter_column('isrctn', column_name=value, new_column_name=key)


def downgrade():
    for key, value in MAPPING.items():
        op.alter_column('isrctn', column_name=key, new_column_name=value)
