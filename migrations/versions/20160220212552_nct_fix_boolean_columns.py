# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op



# revision identifiers, used by Alembic.
revision = '9833dacb0b30'
down_revision = u'820db6031f39'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE nct ALTER COLUMN is_fda_regulated TYPE boolean USING is_fda_regulated::boolean')
    op.execute('ALTER TABLE nct ALTER COLUMN is_section_801 TYPE boolean USING is_section_801::boolean')
    op.execute('ALTER TABLE nct ALTER COLUMN has_expanded_access TYPE boolean USING has_expanded_access::boolean')


def downgrade():
    pass
