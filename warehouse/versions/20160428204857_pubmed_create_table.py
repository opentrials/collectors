# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b720671a8c0f'
down_revision = u'014fd3f703aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('pubmed',

        # Meta

        sa.Column('meta_id', sa.Text, unique=True),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # Medline

        sa.Column('pmid', sa.Text, primary_key=True),
        sa.Column('date_created', sa.Date),
        sa.Column('date_completed', sa.Date),
        sa.Column('date_revised', sa.Date),
        sa.Column('country', sa.Text),
        sa.Column('medline_ta', sa.Text),
        sa.Column('nlm_unique_id', sa.Text),
        sa.Column('issn_linking', sa.Text),

        # Journal

        sa.Column('journal_issn', sa.Text),
        sa.Column('journal_title', sa.Text),
        sa.Column('journal_iso', sa.Text),

        # Article

        sa.Column('article_title', sa.Text),
        sa.Column('article_abstract', sa.Text),
        sa.Column('article_authors', ARRAY(sa.Text)),
        sa.Column('article_language', sa.Text),
        sa.Column('article_publication_type_list', ARRAY(sa.Text)),
        sa.Column('article_vernacular_title', sa.Text),
        sa.Column('article_date', sa.Date),

        # Pubmed

        sa.Column('publication_status', sa.Text),
        sa.Column('identifiers_list', JSONB()),

    )


def downgrade():
    op.drop_table('pubmed')
