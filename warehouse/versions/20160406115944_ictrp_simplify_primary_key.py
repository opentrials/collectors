# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '00d329f5f40a'
down_revision = u'58d2189bc678'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('ictrp_pkey', 'ictrp')
    op.create_primary_key('ictrp_pkey', 'ictrp', ['main_id'])


def downgrade():
    op.drop_constraint('ictrp_pkey', 'ictrp')
    op.create_primary_key('ictrp_pkey', 'ictrp', ['register', 'main_id'])
