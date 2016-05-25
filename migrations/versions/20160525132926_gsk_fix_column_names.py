# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = 'f736bb9d2499'
down_revision = u'e77e7eaf0a34'
branch_labels = None
depends_on = None

MAPPING = {
    'clinicaltrials_gov_identifier': 'clinicaltrialsgov_identifier',
    'ind_ide_protocol': 'indide_protocol',
    'ind_ide_grantor': 'indide_grantor',
    'ind_ide_number': 'indide_number',
    'ind_ide_serial_number': 'indide_serial_number',
    'responsible_party_name_official_title': 'responsible_party_nameofficial_title',
    'trade_name_product_name': 'trade_name__product_name',
}


def upgrade():
    for key, value in MAPPING.items():
        op.alter_column('gsk', column_name=value, new_column_name=key)


def downgrade():
    for key, value in MAPPING.items():
        op.alter_column('gsk', column_name=key, new_column_name=value)
