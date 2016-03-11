# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean, Integer, Json, Array  # noqa


# Module API

class Item(base.Item):

    # Config

    table = 'data_pfizer'
    primary_key = 'nct_id'
    updated_key = None
    ensure_fields = False

    # General

    title = Text()

    # Description

    study_type = Text()
    organization_id = Text()
    nct_id = Text()
    status = Text()
    study_start_date = Date('%B, %Y')
    study_end_date = Date('%B, %Y')

    # Eligibility

    eligibility_criteria = Text()
    gender = Text()
    age_range = Text()
    healthy_volunteers_allowed = Boolean('Accepts Healthy Volunteers')
