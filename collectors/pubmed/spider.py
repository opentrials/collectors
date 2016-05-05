# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
from urllib import urlencode
from datetime import datetime, date, timedelta
from collections import OrderedDict
from scrapy.spiders import CrawlSpider
from .parser import parse_record
logger = logging.getLogger(__name__)


# Module API

class PubmedSpider(CrawlSpider):

    # Public

    name = 'pubmed'
    allowed_domains = ['eutils.ncbi.nlm.nih.gov']

    def __init__(self, conn=None, date_from=None, date_to=None):

        # Save conn dict
        self.conn = conn

        # Make start urls
        self.start_urls = _make_start_urls(
            prefix='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/',
            template='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id={pmid}&retmode=xml',
            date_from=date_from, date_to=date_to)

        # Set parser
        self.parse = parse_record

        # Inherit parent
        super(PubmedSpider, self).__init__()


# Internal

def _make_start_urls(prefix, template, date_from=None, date_to=None):
    """ Return start_urls.
    """

    # Prepare dates
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    date_from = datetime.strptime(date_from, '%Y-%m-%d').strftime('%Y/%m/%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d').strftime('%Y/%m/%d')

    # Prepare query
    # TODO: here we could use more smart method -
    # search for wildcarded nct10[0-9]*, isrctn1[0-9]* etc
    # we need cycle here because max 600 identifiers could be used
    # in one Pubmed search
    query = OrderedDict()
    query['db'] = 'pubmed'
    query['term'] = 'trial registration'  # TODO: review
    query['retmode'] = 'json'
    query['datetype'] = 'pdat'  # TODO: review
    query['mindate'] = date_from
    query['maxdate'] = date_to
    query['retmax'] = '100000'

    # Make request
    res = requests.get(prefix + '?' + urlencode(query))
    pmids = res.json()['esearchresult']['idlist']
    urls = []
    for pmid in pmids:
        urls.append(template.format(pmid=pmid))
    logger.info('Populated Pubmed start urls: %s', len(urls))
    return urls
