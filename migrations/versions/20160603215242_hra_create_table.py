# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4c0db99bb1c'
down_revision = u'6d709931cc58'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('hra',

        # Meta

        sa.Column('meta_id', sa.Text, unique=True),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('hra_id', sa.Text),
        sa.Column('publication_date', sa.Date),
        sa.Column('updated_date', sa.Date),
        sa.Column('comittee_name', sa.Text),
        sa.Column('comittee_ref_number', sa.Text),
        sa.Column('iras_proj_id', sa.Text),
        sa.Column('contact_name', sa.Text),
        sa.Column('contact_email', sa.Text),
        sa.Column('application_title', sa.Text),
        sa.Column('study_type_id', sa.Text),
        sa.Column('study_type', sa.Text),
        sa.Column('sponsor_org', sa.Text),
        sa.Column('research_programme', sa.Text),
        sa.Column('data_coll_arrangements', sa.Text),
        sa.Column('establishment_org', sa.Text),
        sa.Column('establishment_org_address_1', sa.Text),
        sa.Column('establishment_org_address_2', sa.Text),
        sa.Column('establishment_org_address_3', sa.Text),
        sa.Column('establishment_org_post_code', sa.Text),
        sa.Column('decision', sa.Text),
        sa.Column('decision_date', sa.DateTime(timezone=True)),
        sa.Column('human_tissue_license', sa.Text),
        sa.Column('rtb_title', sa.Text),
        sa.Column('research_database_title', sa.Text),
        sa.Column('application_full_title', sa.Text),
        sa.Column('isrctn_id', sa.Text),
        sa.Column('nct_id', sa.Text),
        sa.Column('additional_ref_numbers', sa.Text),
        sa.Column('duration_of_study_in_uk', sa.Text),
        sa.Column('research_summary', sa.Text),
        sa.Column('euctr_id', sa.Text),
        sa.Column('social_value', sa.Text),
        sa.Column('recuitment_arrangements', sa.Text),
        sa.Column('risk_and_benefit', sa.Text),
        sa.Column('participants_protection_and_care', sa.Text),
        sa.Column('informed_consent', sa.Text),
        sa.Column('applicant_and_staff_suitability', sa.Text),
        sa.Column('independent_review', sa.Text),
        sa.Column('supporting_info_suitability', sa.Text),
        sa.Column('other_comments', sa.Text),
        sa.Column('research_summary_suitability', sa.Text),

    )


def downgrade():
    op.drop_table('hra')
