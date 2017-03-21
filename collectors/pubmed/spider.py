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

class Spider(CrawlSpider):

    # Public

    name = 'pubmed'
    allowed_domains = ['eutils.ncbi.nlm.nih.gov']

    def __init__(self, conf=None, conn=None, date_from=None, date_to=None):

        # Save conf/conn
        self.conf = conf
        self.conn = conn

        # Make start urls
        self.start_urls = _make_start_urls(
            prefix='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/',
            template='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id={pmid}&retmode=xml',
            date_from=date_from, date_to=date_to)

        # Set parser
        self.parse = parse_record

        # Inherit parent
        super(Spider, self).__init__()


# Internal

def _make_start_urls(prefix, template, date_from=None, date_to=None, session=None):
    """ Return start_urls.
    """

    # Init urls and session
    urls = set()
    if not session:
        session = requests.Session()
    adapter_opts = {'max_retries': requests.packages.urllib3.util.Retry(total=5, status_forcelist=[503])}
    session.mount('https://', requests.adapters.HTTPAdapter(**adapter_opts))

    # Prepare dates
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    date_from = datetime.strptime(date_from, '%Y-%m-%d').strftime('%Y/%m/%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d').strftime('%Y/%m/%d')

    # Prepare query
    query = OrderedDict()
    query['db'] = 'pubmed'
    query['retmode'] = 'json'
    query['mindate'] = date_from
    query['maxdate'] = date_to

    # Terms to search
    query['term'] = """(randomized controlled trial[Publication Type] OR
                        (randomized[Title/Abstract]
                         AND controlled[Title/Abstract]
                         AND trial[Title/Abstract]
                        ))
                    """

    # For both publication/modifiction
    for date_type in ['pdat', 'mdat']:
        retstart = 0
        retmax = 50000
        while True:
            query['datetype'] = date_type
            query['retstart'] = retstart
            query['retmax'] = retmax
            url = '%s?%s' % (prefix, urlencode(query))
            response = session.get(url)
            pmids = response.json()['esearchresult']['idlist']
            if not pmids:
                break
            for pmid in pmids:
                urls.add(template.format(pmid=pmid))
            retstart += retmax

    # Log urls count
    logger.info('Populated Pubmed start urls: %s', len(urls))

    return list(urls)
