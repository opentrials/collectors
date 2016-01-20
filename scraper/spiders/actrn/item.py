# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy


class Item(scrapy.Item):

    # Plain value fields

    trial_id = scrapy.Field()
    ethics_application_status = scrapy.Field()
    date_submitted = scrapy.Field()
    date_registered = scrapy.Field()
    type_of_registration = scrapy.Field()
    procedure_for_enrolling_a_subject_and_allocating_the = scrapy.Field()
    methods_used_to_generate_the_sequence_in_which = scrapy.Field()
    intervention_assignment = scrapy.Field()
    primary_sponsor_type = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    country = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    country = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    country = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    country = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()

    # Helpers

    def __repr__(self):
        template = '<ACTRN: %s [%s]>'
        text = template % (
                self.get('trial_id'),
                self.get('date_registered'))
        return text

    def add_data(self, key, value):
        if key in self.fields:
            self[key] = value
