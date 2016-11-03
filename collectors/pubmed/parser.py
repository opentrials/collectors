# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import xmltodict
from dateutil.parser import parse as date_parse
from .record import Record


# Module API

def parse_record(res):

    # Init data
    data = {}

    # Parse xml
    parsed_data = xmltodict.parse(res.body, force_cdata=True, dict_constructor=dict)
    if 'PubmedArticle' not in parsed_data['PubmedArticleSet']:
        return None
    medline = parsed_data['PubmedArticleSet']['PubmedArticle']['MedlineCitation']
    pubmed = parsed_data['PubmedArticleSet']['PubmedArticle']['PubmedData']
    article = medline['Article']
    journal = article['Journal']

    # Medline

    data['pmid'] = medline['PMID']['#text']
    if 'DateCreated' in medline:
        data['date_created'] = '{year}-{month}-{day}'.format(
            year=medline['DateCreated']['Year']['#text'],
            month=medline['DateCreated']['Month']['#text'],
            day=medline['DateCreated']['Day']['#text'])
    if 'DateCompleted' in medline:
        data['date_completed'] = '{year}-{month}-{day}'.format(
            year=medline['DateCompleted']['Year']['#text'],
            month=medline['DateCompleted']['Month']['#text'],
            day=medline['DateCompleted']['Day']['#text'])
    if 'DateRevised' in medline:
        data['date_revised'] = '{year}-{month}-{day}'.format(
            year=medline['DateRevised']['Year']['#text'],
            month=medline['DateRevised']['Month']['#text'],
            day=medline['DateRevised']['Day']['#text'])
    if medline['MedlineJournalInfo'].get('Country'):
        data['country'] = medline['MedlineJournalInfo']['Country']['#text']
    if 'MedlineTA' in medline['MedlineJournalInfo']:
        data['medline_ta'] = medline['MedlineJournalInfo']['MedlineTA']['#text']
    if 'NlmUniqueID' in medline['MedlineJournalInfo']:
        data['nlm_unique_id'] = medline['MedlineJournalInfo']['NlmUniqueID']['#text']
    if 'ISSNLinking' in medline['MedlineJournalInfo']:
        data['issn_linking'] = medline['MedlineJournalInfo']['ISSNLinking']['#text']
    if 'MeshHeadingList' in medline:
        data['mesh_headings'] = medline['MeshHeadingList']

    # Journal

    if 'ISSN' in journal:
        data['journal_issn'] = journal['ISSN']['#text']
    if 'Title' in journal:
        data['journal_title'] = journal['Title']['#text']
    if 'ISOAbbreviation' in journal:
        data['journal_iso'] = journal['ISOAbbreviation']['#text']

    # Article

    if 'ArticleTitle' in article:
        data['article_title'] = article['ArticleTitle']['#text']
    if 'Abstract' in article:
        elem = article['Abstract']['AbstractText']
        if not isinstance(elem, list):
            elem = [elem]
        text = [subelem['#text'] for subelem in elem
                if '#text' in subelem]
        data['article_abstract'] = ' '.join(text)
    if 'AuthorList' in article:
        data['article_authors'] = []
        for item in article['AuthorList']['Author']:
            if 'ForeName' in item and 'LastName' in item:
                data['article_authors'].append('%s %s' % (
                    item['ForeName']['#text'], item['LastName']['#text']))
    if 'Language' in article:
        elem = article['Language']
        if not isinstance(elem, list):
            elem = [elem]
        # FIXME: Properly handle multiple languages
        data['article_language'] = elem[0]['#text']
    if 'PublicationTypeList' in article:
        data['article_publication_type_list'] = []
        elem = article['PublicationTypeList']['PublicationType']
        if not isinstance(elem, list):
            elem = [elem]
        for sumelem in elem:
            data['article_publication_type_list'].append(sumelem['#text'])
    if article.get('VernacularTitle'):
        data['article_vernacular_title'] = article['VernacularTitle']['#text']
    if 'ArticleDate' in article:
        article_date = '{year}-{month}-{day}'.format(
            year=article['ArticleDate']['Year']['#text'],
            month=article['ArticleDate']['Month']['#text'],
            day=article['ArticleDate']['Day']['#text'])
        article_date = date_parse(article_date)
        data['article_date'] = article_date.strftime('%Y-%m-%d')

    # Pubmed

    if 'PublicationStatus' in pubmed:
        data['publication_status'] = pubmed['PublicationStatus']['#text']
    if 'ArticleIdList' in pubmed:
        data['identifiers_list'] = {}
        items = pubmed['ArticleIdList']['ArticleId']
        if not isinstance(items, list):
            items = [items]
        for item in items:
            data['identifiers_list'][item['@IdType']] = item['#text']

    # Create record
    url = 'http://www.ncbi.nlm.nih.gov/pubmed/%s' % data['pmid']
    record = Record.create(url, data)

    return record


# Internal

def _parse_first(res, path, element='text()'):
    return res.xpath('%s/%s' % (path, element)).extract_first()
