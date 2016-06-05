# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean, Integer, Json, Array


# Module API

class Record(base.Record):

    # Config

    table = 'actrn'
    primary_key = 'trial_id'
    ensure_fields = False

    # General

    trial_id = Text()
    ethics_application_status = Text()
    date_submitted = Date('%d/%m/%Y')
    date_registered = Date('%d/%m/%Y')
    type_of_registration = Text()

    # Titles & IDs

    public_title = Text()
    scientific_title = Text()
    secondary_ids = Array()
    universal_trial_number_utn = Text()
    trial_acronym = Text()

    # Health condition

    health_conditions_or_problems_studied = Text()
    condition_category = Text()
    condition_code = Text()

    # Intervention/exposure

    study_type = Text()
    patient_registry = Boolean('Yes')
    target_follow_up_duration = Integer()
    target_follow_up_type = Text()
    description_of_intervention_s_exposure = Text()
    intervention_codes = Array()
    comparator_control_treatment = Text()
    control_group = Text()

    # Outcomes

    primary_outcomes = Json()
    secondary_outcomes = Json()

    # Eligibility

    key_inclusion_criteria = Text()
    minimum_age = Text()
    maximum_age = Text()
    gender = Text()
    can_healthy_volunteers_participate = Boolean('Yes')
    key_exclusion_criteria = Text()

    # Study design

    purpose_of_the_study = Text()
    allocation_to_intervention = Text()
    procedure_for_enrolling_a_subject_and_allocating_the_treatment_ = Text()
    methods_used_to_generate_the_sequence_in_which_subjects_will_be = Text()
    masking_blinding = Text()
    who_is_are_masked_blinded = Text()
    intervention_assignment = Text()
    other_design_features = Text()
    phase = Text()
    type_of_endpoint_s = Text()
    purpose = Text()
    duration = Text()
    selection = Text()
    timing = Text()
    statistical_methods_analysis = Text()

    # Recruitment

    anticipated_date_of_first_participant_enrolment = Date('%d/%m/%Y')
    actual_date_of_first_participant_enrolment = Date('%d/%m/%Y')
    anticipated_date_last_participant_enrolled = Date('%d/%m/%Y')
    actual_date_last_participant_enrolled = Date('%d/%m/%Y')
    target_sample_size = Integer()
    actual_sample_size = Integer()
    recruitment_status = Text()
    recruitment_state_s = Text()

    # Funding & Sponsors

    primary_sponsor = Json()
    sponsors = Json()

    # Ethics approval

    ethics_application_status = Text()
    ethics_applications = Json()

    # Summary

    brief_summary = Text()
    trial_website = Text()
    trial_related_presentations_publications = Text()
    public_notes = Text()
    attachments = Array()

    # Contacts

    principal_investigator = Json()
    public_queries = Json()
    scientific_queries = Json()
