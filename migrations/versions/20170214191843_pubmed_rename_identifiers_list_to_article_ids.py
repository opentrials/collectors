# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op


# revision identifiers, used by Alembic.
revision = '3dbb46f23ed7'
down_revision = u'0087dc1eb534'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('pubmed', 'identifiers_list', new_column_name='article_ids')


def downgrade():
    op.alter_column('pubmed', 'article_ids', new_column_name='identifiers_list')
