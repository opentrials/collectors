# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .item import Item


# Module API

class Mapper(base.Mapper):

    # Public

    ignore = [
        'subject_number_of_subjects_for_this_age_range',
        'subject_trial_has_subjects_under_18',
        'subject_in_utero',
        'subject_preterm_newborn_infants_up_to_gestational_age_',
        'subject_newborns_027_days',
        'subject_infants_and_toddlers_28_days23_months',
        'subject_children_211years',
        'subject_adolescents_1217_years',
        'subject_adults_1864_years',
        'subject_elderly_65_years',
        'subject_women_of_childbearing_potential_not_using_contraception_for',
    ]

    def map_response(self, res):

        # Init data item
        data = {}

        # Summary

        kpath = '.cellGrey'
        vpath = '.cellGrey+.cellLighterGrey'
        subdata = utils.extract_dict(res, kpath, vpath)
        subdata['eudract_number_with_country'] = res.url.split('/')[-1]
        data.update(subdata)

        key = 'eudract_number_with_country'
        value = '-'.join([data['eudract_number'], res.url.split('/')[-1]])
        data.update({key: value})

        # A. Protocol Information

        ident = 'section-a'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        data.update(subdata)

        # B. Sponsor information

        key = 'sponsors'
        ident = 'section-b'
        kpath = '.second'
        vpath = '.second+.third'
        first = 'name_of_sponsor'
        table = utils.select_table(res, ident)
        value = utils.extract_list(table, kpath, vpath, first)
        data.update({key: value})

        # C. Applicant Identification

        # ...

        # D. IMP Identification

        key = 'imps'
        ident = 'section-d'
        kpath = '.second'
        vpath = '.second+.third'
        first = 'imp_role'
        table = utils.select_table(res, ident)
        value = utils.extract_list(table, kpath, vpath, first)
        data.update({key: value})

        # D8. Information on Placebo

        key = 'placebos'
        ident = 'section-d8'
        kpath = '.second'
        vpath = '.second+.third'
        first = 'is_a_placebo_used_in_this_trial'
        table = utils.select_table(res, ident)
        value = utils.extract_list(table, kpath, vpath, first)
        data.update({key: value})

        # E. General Information on the Trial

        ident = 'section-e'
        kpath = '.second'
        vpath = '.second+.third'
        prefix = 'trial_'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath, prefix)
        data.update(subdata)

        # F. Population of Trial Subjects

        ident = 'section-f'
        kpath = '.second'
        vpath = '.second+.third'
        prefix = 'subject_'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath, prefix)
        data.update(subdata)

        code = 'F.1.1'
        key = 'subject_childs'
        value = utils.extract_value(table, code, index=1)
        subdata[key] = value

        code = 'F.1.2.1'
        key = 'subject_adults'
        value = utils.extract_value(table, code)
        subdata[key] = value

        code = 'F.1.3.1'
        key = 'subject_elderly'
        value = utils.extract_value(table, code)
        subdata[key] = value

        data.update(subdata)

        # G. Investigator Networks to be involved in the Trial

        # ...

        # N. Review by the Competent Authority or Ethics Committee

        ident = 'section-n'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        data.update(subdata)

        # P. End of Trial

        ident = 'section-p'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        data.update(subdata)

        # Remove ignored data
        for key in self.ignore:
            if key in data:
                del data[key]

        # Create item
        item = Item.create(res.url, data)

        return item
