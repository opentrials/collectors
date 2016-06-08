# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Datetime


# Module API

class Record(base.Record):

    # Config

    table = 'hra'

    # General

    hra_id = Text(primary_key=True)
    publication_date = Date('%Y-%m-%dT%H:%M:%S')
    updated_date = Date('%Y-%m-%dT%H:%M:%S.%f')
    comittee_name = Text()
    comittee_ref_number = Text()
    iras_proj_id = Text()
    contact_name = Text()
    contact_email = Text()
    application_title = Text()
    study_type_id = Text()
    study_type = Text()
    sponsor_org = Text()
    research_programme = Text()
    data_coll_arrangements = Text()
    establishment_org = Text()
    establishment_org_address_1 = Text()
    establishment_org_address_2 = Text()
    establishment_org_address_3 = Text()
    establishment_org_post_code = Text()
    decision = Text()
    decision_date = Datetime('%Y-%m-%d %H:%M:%S')
    human_tissue_license = Text()
    rtb_title = Text()
    research_database_title = Text()
    application_full_title = Text()
    isrctn_id = Text()
    nct_id = Text()
    additional_ref_numbers = Text()
    duration_of_study_in_uk = Text()
    research_summary = Text()
    euctr_id = Text()
    social_value = Text()
    recuitment_arrangements = Text()
    risk_and_benefit = Text()
    participants_protection_and_care = Text()
    informed_consent = Text()
    applicant_and_staff_suitability = Text()
    independent_review = Text()
    supporting_info_suitability = Text()
    other_comments = Text()
    research_summary_suitability = Text()
