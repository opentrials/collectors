# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from .record import Record
logger = logging.getLogger(__name__)


def parse_record(url, item):

    # Init data
    data = {}

    # Map data
    data['hra_id'] = 'HRA%s' % item['ApplicationID']
    data['publication_date'] = item['PublicationDate']
    data['updated_date'] = item['UpdatedDate']
    data['comittee_name'] = item['CommitteeName']
    data['comittee_ref_number'] = item['CommitteeReferenceNumber']
    data['iras_proj_id'] = item['IrasProjectID']
    data['contact_name'] = item['ContactName']
    data['contact_email'] = item['ContactEmail']
    data['application_title'] = item['ApplicationTitle']
    data['study_type_id'] = item['StudyTypeID']
    data['study_type'] = item['StudyType']
    data['sponsor_org'] = item['SponsorOrganisation']
    data['research_programme'] = item['ResearchProgramme']
    data['data_coll_arrangements'] = item['DataCollectionArrangements']
    data['establishment_org'] = item['EstablishmentOrganisation']
    data['establishment_org_address_1'] = item['EstablishmentOrganisationAddress1']
    data['establishment_org_address_2'] = item['EstablishmentOrganisationAddress2']
    data['establishment_org_address_3'] = item['EstablishmentOrganisationAddress3']
    data['establishment_org_post_code'] = item['EstablishmentOrganisationPostcode']
    data['decision'] = item['Decision']
    data['decision_date'] = item['DecisionDate']
    data['human_tissue_license'] = item['HumanTissueAuthorityStorageLicence']
    data['rtb_title'] = item['RTBTitle']
    data['research_database_title'] = item['ResearchDatabaseTitle']
    data['application_full_title'] = item['ApplicationFullTitle']
    data['isrctn_id'] = item['ISRCTN']
    data['nct_id'] = item['NCT']
    data['additional_ref_numbers'] = item['AdditionalReferenceNumbers']
    data['duration_of_study_in_uk'] = item['DurationOfStudyInUK']
    data['research_summary'] = item['ResearchSummary']
    data['euctr_id'] = item['EudraCT']
    data['social_value'] = item['SocialValue']
    data['recuitment_arrangements'] = item['RecruitmentArrangements']
    data['risk_and_benefit'] = item['RiskAndBenefit']
    data['participants_protection_and_care'] = item['ParticipantsProtectionAndCare']
    data['informed_consent'] = item['InformedConsent']
    data['applicant_and_staff_suitability'] = item['ApplicantAndStaffSuitability']
    data['independent_review'] = item['IndependentReview']
    data['supporting_info_suitability'] = item['SupportingInfoSuitability']
    data['other_comments'] = item['OtherComments']
    data['research_summary_suitability'] = item['ResearchSummarySuitability']

    # Create record
    record = Record.create(url, data)

    return record
