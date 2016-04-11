# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op


# revision identifiers, used by Alembic.
revision = '296d1e273220'
down_revision = u'3433d4d2a0d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('isrctn',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('isrctn_id', sa.Text, primary_key=True),
        sa.Column('doi_isrctn_id', sa.Text),
        sa.Column('title', sa.Text),
        sa.Column('condition_category', sa.Text),
        sa.Column('date_applied', sa.Date),
        sa.Column('date_assigned', sa.Date),
        sa.Column('last_edited', sa.Date),
        sa.Column('prospectiveretrospective', sa.Text),
        sa.Column('overall_trial_status', sa.Text),
        sa.Column('recruitment_status', sa.Text),
        sa.Column('plain_english_summary', sa.Text),
        sa.Column('trial_website', sa.Text),

        # Contant information

        sa.Column('contacts', JSONB),

        # Additional identifiers

        sa.Column('eudract_number', sa.Text),
        sa.Column('clinicaltrialsgov_number', sa.Text),
        sa.Column('protocolserial_number', sa.Text),

        # Study information

        sa.Column('scientific_title', sa.Text),
        sa.Column('acronym', sa.Text),
        sa.Column('study_hypothesis', sa.Text),
        sa.Column('ethics_approval', sa.Text),
        sa.Column('study_design', sa.Text),
        sa.Column('primary_study_design', sa.Text),
        sa.Column('secondary_study_design', sa.Text),
        sa.Column('trial_setting', sa.Text),
        sa.Column('trial_type', sa.Text),
        sa.Column('patient_information_sheet', sa.Text),
        sa.Column('condition', sa.Text),
        sa.Column('intervention', sa.Text),
        sa.Column('intervention_type', sa.Text),
        sa.Column('phase', sa.Text),
        sa.Column('drug_names', sa.Text),
        sa.Column('primary_outcome_measures', sa.Text),
        sa.Column('secondary_outcome_measures', sa.Text),
        sa.Column('overall_trial_start_date', sa.Date),
        sa.Column('overall_trial_end_date', sa.Date),
        sa.Column('reason_abandoned', sa.Text),

        # Eligability

        sa.Column('participant_inclusion_criteria', sa.Text),
        sa.Column('participant_type', sa.Text),
        sa.Column('age_group', sa.Text),
        sa.Column('gender', sa.Text),
        sa.Column('target_number_of_participants', sa.Text),
        sa.Column('participant_exclusion_criteria', sa.Text),
        sa.Column('recruitment_start_date', sa.Date),
        sa.Column('recruitment_end_date', sa.Date),

        # Locations

        sa.Column('countries_of_recruitment', sa.Text),
        sa.Column('trial_participating_centre', sa.Text),

        # Sponsor information

        sa.Column('sponsors', JSONB),

        # Funders

        sa.Column('funders', JSONB),

        # Results and publications

        sa.Column('publication_and_dissemination_plan', sa.Text),
        sa.Column('intention_to_publish_date', sa.Date),
        sa.Column('participant_level_data', sa.Text),
        sa.Column('results_basic_reporting', sa.Text),
        sa.Column('publication_summary', sa.Text),
        sa.Column('publication_citations', sa.Text),

    )


def downgrade():
    op.drop_table('isrctn')
