# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from alembic import op



# revision identifiers, used by Alembic.
revision = '33a5e999fd54'
down_revision = u'babb1b77ca56'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('jprn',

        # Meta

        sa.Column('meta_uuid', sa.Text),
        sa.Column('meta_source', sa.Text),
        sa.Column('meta_created', sa.DateTime(timezone=True)),
        sa.Column('meta_updated', sa.DateTime(timezone=True)),

        # General

        sa.Column('recruitment_status', sa.Text),
        sa.Column('unique_trial_number', sa.Text, primary_key=True),
        sa.Column('title_of_the_study', sa.Text),
        sa.Column('date_of_formal_registrationdate_of_icmje_and_who', sa.Date),
        sa.Column('date_and_time_of_last_update', sa.DateTime(timezone=True)),

        # Basic information

        sa.Column('official_scientific_title_of_the_study', sa.Text),
        sa.Column('title_of_the_study_brief_title', sa.Text),
        sa.Column('region', sa.Text),

        # Condition

        sa.Column('condition', sa.Text),
        sa.Column('classification_by_specialty', sa.Text),
        sa.Column('classification_by_malignancy', sa.Text),
        sa.Column('genomic_information', sa.Boolean),

        # Objectives

        sa.Column('narrative_objectives1', sa.Text),
        sa.Column('basic_objectives2', sa.Text),
        sa.Column('basic_objectives_others', sa.Text),
        sa.Column('trial_characteristics_1', sa.Text),
        sa.Column('trial_characteristics_2', sa.Text),
        sa.Column('developmental_phase', sa.Text),

        # Assessment

        sa.Column('primary_outcomes', sa.Text),
        sa.Column('key_secondary_outcomes', sa.Text),

        # Base

        sa.Column('study_type', sa.Text),

        # Study design

        sa.Column('basic_design', sa.Text),
        sa.Column('randomization', sa.Text),
        sa.Column('randomization_unit', sa.Text),
        sa.Column('blinding', sa.Text),
        sa.Column('control', sa.Text),
        sa.Column('stratification', sa.Text),
        sa.Column('dynamic_allocation', sa.Text),
        sa.Column('institution_consideration', sa.Text),
        sa.Column('blocking', sa.Text),
        sa.Column('concealment', sa.Text),

        # Intervention

        sa.Column('no_of_arms', sa.Integer),
        sa.Column('purpose_of_intervention', sa.Text),
        sa.Column('type_of_intervention', sa.Text),
        sa.Column('interventions', ARRAY(sa.Text)),

        # Eligibility

        sa.Column('agelower_limit', sa.Text),
        sa.Column('ageupper_limit', sa.Text),
        sa.Column('gender', sa.Text),
        sa.Column('key_inclusion_criteria', sa.Text),
        sa.Column('key_exclusion_criteria', sa.Text),
        sa.Column('target_sample_size', sa.Integer),

        # Research contact person

        sa.Column('research_name_of_lead_principal_investigator', sa.Text),
        sa.Column('research_organization', sa.Text),
        sa.Column('research_division_name', sa.Text),
        sa.Column('research_address', sa.Text),
        sa.Column('research_tel', sa.Text),
        sa.Column('research_homepage_url', sa.Text),
        sa.Column('research_email', sa.Text),

        # Public contact

        sa.Column('public_name_of_contact_person', sa.Text),
        sa.Column('public_organization', sa.Text),
        sa.Column('public_division_name', sa.Text),
        sa.Column('public_address', sa.Text),
        sa.Column('public_tel', sa.Text),
        sa.Column('public_homepage_url', sa.Text),
        sa.Column('public_email', sa.Text),

        # Sponsor

        sa.Column('name_of_primary_sponsor', sa.Text),

        # Funding source

        sa.Column('source_of_funding', sa.Text),
        sa.Column('category_of_org', sa.Text),
        sa.Column('nation_of_funding', sa.Text),

        # Other related organizations

        sa.Column('cosponsor', sa.Text),
        sa.Column('name_of_secondary_funers', sa.Text),

        # Secondary study IDs

        sa.Column('secondary_study_ids', sa.Boolean),
        sa.Column('secondary_study_id_1', sa.Text),
        sa.Column('org_issuing_secondary_study_id_1', sa.Text),
        sa.Column('secondary_study_id_2', sa.Text),
        sa.Column('org_issuing_secondary_study_id_2', sa.Text),
        sa.Column('ind_to_mhlw', sa.Text),

        # Institutions

        sa.Column('institutions', sa.Text),

        # Progress

        sa.Column('recruitment_status', sa.Text),
        sa.Column('date_of_protocol_fixation', sa.Date),
        sa.Column('anticipated_trial_start_date', sa.Date),
        sa.Column('last_followup_date', sa.Date),
        sa.Column('date_of_closure_to_data_entry', sa.Date),
        sa.Column('date_trial_data_considered_complete', sa.Date),
        sa.Column('date_analysis_concluded', sa.Date),

        # Related information

        sa.Column('url_releasing_protocol', sa.Text),
        sa.Column('publication_of_results', sa.Text),
        sa.Column('url_releasing_results', sa.Text),
        sa.Column('results', sa.Text),
        sa.Column('other_related_information', sa.Text),

        # Others

        sa.Column('date_of_registration', sa.Date),
        sa.Column('date_of_last_update', sa.DateTime(timezone=True)),
        sa.Column('urljapanese', sa.Text),
        sa.Column('urlenglish', sa.Text),

)


def downgrade():
    pass
