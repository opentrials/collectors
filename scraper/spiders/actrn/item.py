# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy import Field

from .. import base


# Module API

class Item(base.Item):

    # Config

    table = 'actrn'
    primary_key = 'trial_id'
    updated_key = 'date_registered'

    # Plain value fields

    trial_id = Field()
    ethics_application_status = Field()
    date_submitted = Field()
    date_registered = Field()
    type_of_registration = Field()
    procedure_for_enrolling_a_subject_and_allocating_the = Field()
    methods_used_to_generate_the_sequence_in_which = Field()
    intervention_assignment = Field()
    primary_sponsor_type = Field()
    name = Field()
    address = Field()
    country = Field()
    name = Field()
    address = Field()
    country = Field()
    phone = Field()
    email = Field()
    name = Field()
    address = Field()
    country = Field()
    phone = Field()
    email = Field()
    name = Field()
    address = Field()
    country = Field()
    phone = Field()
    email = Field()
