# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean


# Module API

class Record(base.Record):

    # Config

    table = 'pfizer'
    ensure_fields = False

    # General

    nct_id = Text(primary_key=True)
    title = Text()

    # Description

    study_type = Text()
    organization_id = Text()
    status = Text()
    study_start_date = Date('%B, %Y')
    study_end_date = Date('%B, %Y')

    # Eligibility

    eligibility_criteria = Text()
    gender = Text()
    age_range = Text()
    healthy_volunteers_allowed = Boolean('Accepts Healthy Volunteers')
