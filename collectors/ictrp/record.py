# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Integer, Json, Array


# Module API

class Record(base.Record):

    # Config

    table = 'ictrp'
    primary_key = 'main_id'
    updated_key = 'last_refreshed_on'
    ensure_fields = False

    # Main

    register = Text()
    last_refreshed_on = Date('%d %B %Y')
    main_id = Text()
    date_of_registration = Text()  # non regular format
    primary_sponsor = Text()
    public_title = Text()
    scientific_title = Text()
    date_of_first_enrollment = Text()  # non regular format
    target_sample_size = Integer()
    recruitment_status = Text()
    url = Text()
    study_type = Text()
    study_design = Text()
    study_phase = Text()

    # Additional

    countries_of_recruitment = Array()
    contacts = Json()
    key_inclusion_exclusion_criteria = Text()  # not presented on the site
    health_conditions_or_problems_studied = Array()
    interventions = Array()
    primary_outcomes = Array()
    secondary_outcomes = Array()
    secondary_ids = Array()
    sources_of_monetary_support = Array()
    secondary_sponsors = Array()
