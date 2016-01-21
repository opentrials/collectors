# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from functools import partial
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from . import utils
from .item import Item


class Spider(CrawlSpider):

    # Public

    name = 'nct'
    allowed_domains = ['clinicaltrials.gov']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = utils.make_start_urls(
                base='https://www.clinicaltrials.gov/ct2/results',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=utils.make_pattern('ct2/results'),
            )),
            Rule(LinkExtractor(
                allow=r'ct2/show/NCT\d+',
                process_value=lambda value: value+'&resultsxml=true',
            ), callback='parse_item'),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Create item
        item = Item()

        # Extraction tools
        gtext = partial(utils.get_text, res)
        gdict = partial(utils.get_dict, res)
        glist = partial(utils.get_list, res)

        # Plain value fields
        item['download_date'] = gtext('required_header/download_date')
        item['link_text'] = gtext('required_header/link_text')
        item['url'] = gtext('required_header/url')
        item['org_study_id'] = gtext('id_info/org_study_id')
        item['nct_id'] = gtext('id_info/nct_id')
        item['brief_title'] = gtext('brief_title')
        item['acronym'] = gtext('acronym')
        item['official_title'] = gtext('official_title')
        item['source'] = gtext('source')
        item['brief_summary'] = gtext('brief_summary/textblock')
        item['detailed_description'] = gtext('detailed_description/textblock')
        item['overall_status'] = gtext('overall_status')
        item['why_stopped'] = gtext('why_stopped')
        item['start_date'] = gtext('start_date')
        item['completion_date_actual'] = gtext('completion_date[@type="Actual"]')
        item['completion_date_anticipated'] = gtext('completion_date[@type="Anticipated"]')
        item['primary_completion_date_actual'] = gtext('primary_completion_date[@type="Actual"]')
        item['primary_completion_date_anticipated'] = gtext('primary_completion_date[@type="Anticipated"]')
        item['phase'] = gtext('phase')
        item['study_type'] = gtext('study_type')
        item['study_design'] = gtext('study_design')
        item['target_duration'] = gtext('target_duration')
        item['number_of_arms'] = gtext('number_of_arms', process=int)
        item['number_of_groups'] = gtext('number_of_groups', process=int)
        item['enrollment_actual'] = gtext('enrollment[@type="Actual"]', process=int)
        item['enrollment_anticipated'] = gtext('enrollment[@type="Anticipated"]', process=int)
        item['biospec_retention'] = gtext('biospec_retention')
        item['biospec_descr'] = gtext('biospec_descr')
        item['verification_date'] = gtext('verification_date')
        item['lastchanged_date'] = gtext('lastchanged_date')
        item['firstreceived_date'] = gtext('firstreceived_date')
        item['is_fda_regulated'] = gtext('is_fda_regulated')
        item['is_section_801'] = gtext('is_section_801')
        item['has_expanded_access'] = gtext('has_expanded_access')

        # Dict value fields
        item['oversight_info'] = gdict('oversight_info', expand='oversight_info')
        item['eligibility'] = gdict('eligibility', expand='eligibility')
        item['overall_contact'] = gdict('overall_contact', expand='overall_contact')
        item['overall_contact_backup'] = gdict('overall_contact_backup', expand='overall_contact_backup')
        item['responsible_party'] = gdict('responsible_party', expand='responsible_party')
        item['clinical_results'] = gdict('clinical_results', expand='clinical_results')
        item['condition_browse'] = gdict('condition_browse', expand='condition_browse')
        item['intervention_browse'] = gdict('intervention_browse', expand='intervention_browse')

        # List value fields
        item['secondary_ids'] = glist('id_info/secondary_id', expand='secondary_id')
        item['nct_aliases'] = glist('id_info/nct_alias', expand='nct_alias')
        item['sponsors'] = glist('sponsors/child::*')
        item['primary_outcomes'] = glist('primary_outcome', expand='primary_outcome')
        item['secondary_outcomes'] = glist('secondary_outcome', expand='secondary_outcome')
        item['other_outcomes'] = glist('other_outcome', expand='other_outcome')
        item['conditions'] = glist('condition', expand='condition')
        item['arm_groups'] = glist('arm_group', expand='arm_group')
        item['interventions'] = glist('intervention', expand='intervention')
        item['overall_officials'] = glist('overall_official', expand='overall_official')
        item['locations'] = glist('location', expand='location')
        item['location_countries'] = glist('location_countries/child::*', expand='country')
        item['removed_countries'] = glist('removed_countries/child::*', expand='country')
        item['links'] = glist('link', expand='link')
        item['references'] = glist('reference', expand='reference')
        item['results_references'] = glist('results_reference', expand='results_reference')
        item['keywords'] = glist('keyword', expand='keyword')

        return item
