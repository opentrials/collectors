# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import uuid
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
from .record import Record


def parse_record(url, review_file):
    tree = etree.parse(review_file)
    study_robs = []
    studies = []

    # Get risk of bias

    root = tree.getroot()
    doi_id = root.attrib.get('DOI', '')
    quality_item_data_entries = tree.findall('//QUALITY_ITEM_DATA_ENTRY')
    for quality_item_data_entry in quality_item_data_entries:
        study_rob = {
            'study_id': quality_item_data_entry.attrib['STUDY_ID'],
            'modified': quality_item_data_entry.attrib.get('MODIFIED', ''),
            'result': quality_item_data_entry.attrib['RESULT'],
            'group_id': quality_item_data_entry.attrib.get('GROUP_ID', ''),
            'group_name': '',
            'result_description': quality_item_data_entry.findtext('DESCRIPTION/P', ''),
        }
        quality_item = quality_item_data_entry.getparent().getparent()
        study_rob['rob_id'] = quality_item.attrib['ID']
        study_rob['rob_name'] = quality_item.findtext('NAME')
        study_rob['rob_description'] = quality_item.findtext('DESCRIPTION/P', '')
        for group in quality_item.iter('QUALITY_ITEM_DATA_ENTRY_GROUP'):
            group_id = group.attrib.get('ID')
            if group_id == study_rob['group_id']:
                study_rob['group_name'] = group.findtext('NAME')
        study_robs.append(study_rob)

    # Get references

    included_studies = tree.find('//INCLUDED_STUDIES')
    for study in included_studies.iter('STUDY'):
        study_info = {
            'id': uuid.uuid1().hex,
            'doi_id': doi_id,
            'file_name': review_file.name,
            'study_id': study.attrib['ID'],
            'study_type': study.attrib['DATA_SOURCE'],
            'refs': [],
        }
        corresponding_robs = [rob for rob in study_robs
                              if rob['study_id'] == study_info['study_id']]
        study_info['robs'] = corresponding_robs
        for reference in study.iter('REFERENCE'):
            ref = {
                'type': reference.attrib['TYPE'],
                'authors': reference.findtext('AU', ''),
                'title': reference.findtext('TI', ''),
                'source': reference.findtext('SO', ''),
                'year': reference.findtext('YR', ''),
                'vl': reference.findtext('VL', ''),
                'no': reference.findtext('NO', ''),
                'pg': reference.findtext('PG', ''),
                'country': reference.findtext('CY', ''),
                'identifiers': [],
            }
            for identifier in reference.iter('IDENTIFIER'):
                ident = {key.lower(): value for key, value in identifier.items()
                         if key not in ['MODIFIED', 'MODIFIED_BY']}
                ref['identifiers'].append(ident)
            study_info['refs'].append(ref)

        # Create record

        record = Record.create(url, study_info)
        studies.append(record)

    return studies
