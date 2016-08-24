# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import urlparse
import re
import random
from scrapy.utils.url import canonicalize_url
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from .record import Record


class Spider(CrawlSpider):

    name = 'fda_dap'
    allowed_domains = ['accessdata.fda.gov']

    def __init__(self, conf=None, conn=None):
        self.conf = conf
        self.conn = conn

        self.start_urls = _make_start_urls(
            'http://www.accessdata.fda.gov/scripts/cder/drugsatfda/index.cfm?fuseaction=Search.SearchResults_Browse&StepSize=100000&DrugInitial='
        )

        super(Spider, self).__init__()

    def make_requests_from_url(self, url):
        return Request(url, callback=self.parse_search_results)

    def parse_search_results(self, response):
        '''
        When we click on a search result item, it sets a few cookies in our
        session to determine which drug we're looking for, and then redirects
        us to the Drug Details or Overview page (depending if the drug has a
        single or multiple applications).

        If a drug has a single application, the request to its details page can
        be made without any cookies set. However, if it has multiple
        applications, the request needs the cookies that were set when we
        visited the search page, otherwise we'll be redirected back to the
        search page.

        There's no way to know if a drug has single or multiple applications
        based on the search page (i.e. we have to do the request). To handle
        this, we save the original URL and cookies we had when hitting the drug
        URL. If we detect we've been redirected to the search page, we can
        simply re-do the request to the original URL and using the original
        cookies.
        '''
        urls = response.css('.product_table a::attr(href)').extract()
        for url in urls:
            full_url = _join_and_canonicalize_urls(response.url, url)
            meta = {
                'cookiejar': random.random(),
                'original_url': full_url,
                'original_cookies': _response_cookies_to_dict(response),
            }
            yield Request(
                full_url,
                meta=meta,
                dont_filter=True,
                callback=self.parse_drug_details_or_overview
            )

    def parse_drug_details_or_overview(self, response):
        '''
        Delegate the parsing of the response depending on what page we're in.
        If we're in the search page, it means the previous request needed some
        cookies that we haven't passed in. In that case, we re-do the request
        with those cookies and a new CookieJar (so subsequent cookies are
        isolated). For more details, check the docs for "parse_search_results".
        '''
        has_single_application = 'Search.DrugDetails' in response.url
        has_multiple_applications = 'Search.Overview' in response.url
        in_search_page = 'Search.Search_Drug_Name' in response.url

        if has_single_application:
            return self.parse_drug_details(response)
        elif has_multiple_applications:
            return self.parse_drug_overview(response)
        elif in_search_page:
            meta = {
                'cookiejar': random.random(),
            }
            return Request(
                response.meta['original_url'],
                cookies=response.meta['original_cookies'],
                meta=meta,
                dont_filter=True,
                callback=self.parse_drug_details_or_overview
            )
        else:
            msg = 'Don\'t know how to handle URL (%s)' % response.url
            raise Exception(msg)

    def parse_drug_details(self, response):
        '''
        We're getting closer! We're already on the drug details page, now we
        just need to look for the Approval History link (if it exists). The
        state is still kept in the cookies, so we need to make sure we're using
        the same CookieJar as the one used on the request here.
        '''
        url_candidates = response.css('#user_provided li > a::attr(href)').extract()
        for url in url_candidates:
            if 'Search.Label_ApprovalHistory' in url:
                meta = {
                    'cookiejar': response.meta.get('cookiejar'),
                }
                return Request(
                    _join_and_canonicalize_urls(response.url, url),
                    meta=meta,
                    dont_filter=True,
                    callback=self.parse_approval_history
                )

    def parse_drug_overview(self, response):
        '''
        This page contains multiple applications for a single drug. We need to
        go to the Drug Details page of each one of those. When we click on a
        link here, we're redirected to a page which sets the state (in the
        cookies) to the drug's details, and then redirect us to the drug details
        page. To avoid the requests messing up with each other, we need a clean
        set of cookies for each one.
        '''
        selector = (
            'table[summary="Drugs by Application Number data table"]'
            ' tr > td:first-child'
            ' a::attr(href)'
        )
        urls = response.css(selector).extract()
        for url in urls:
            meta = {
                'cookiejar': random.random(),
            }
            yield Request(
                _join_and_canonicalize_urls(response.url, url),
                meta=meta,
                dont_filter=True,
                callback=self.parse_drug_details_or_overview
            )

    def parse_approval_history(self, response):
        '''
        In this page we're looking for the FDA application number and each row
        in the approval history table. Some of the rows have links to documents
        or another pages (mainly the Drug Approval Package pages), however we
        want all documents to have direct links to their PDFs (makes it easier
        for the processors).

        To do so, we call the "expand_approval_history_documents" method on
        each row item we parsed. It'll check if there're any documents with
        links that don't point to PDFs and, if so, will go to those pages and
        parse the PDF links from them.
        '''
        _extract_text = lambda selector: selector.css('::text') \
                                                 .extract_first() \
                                                 .strip()

        def _parse_links(selector):
            names = [_clean_document_name(name)
                     for name in selector.css('a::text').extract()]
            urls = [url.strip()
                    for url in selector.css('a::attr(href)').extract()]
            msg = 'The number of document names and URLs is different (%d != %d)' % (len(names), len(urls))
            assert len(names) == len(urls), msg

            return [{'name': name, 'urls': [url]}
                    for name, url in zip(names, urls)]

        def _parse_row(row, url, fda_application_num):
            columns = row.css('td')

            data = {
                'fda_application_num': fda_application_num,
                'action_date': _extract_text(columns[0]),
                'supplement_number': _extract_text(columns[1]),
                'approval_type': _extract_text(columns[2]),
                'documents': _parse_links(columns[3]),
                'notes': _extract_text(columns[4]) or None,
            }
            data['id'] = '-'.join([data['fda_application_num'],
                                   data['supplement_number']])

            return Record.create(None, data)

        def _parse_fda_application_num(res):
            drug_details = res.css('.details_table strong::text')
            assert len(drug_details) >= 4, \
                'We expected more drug details (%d < 4)' % len(drug_details)
            return re.sub(r'[()\s]', '', drug_details[3].extract())

        fda_application_num = _parse_fda_application_num(response)
        selector = 'table[summary="Approval History for the selected Application"] tr'
        rows = response.css(selector)
        items = [_parse_row(row, response.url, fda_application_num)
                 for row in rows[1:-1]]  # Ignore table's header and footer

        for item in items:
            yield self.expand_approval_history_documents(item)

    def expand_approval_history_documents(self, item):
        '''Returns the unmodified item if all documents' URLs points to a PDF,
        otherwise returns a Request for that URL and "parse_dap_page" as
        callback.

        This function checks all documents' URLs looking for the ones that don't
        point to PDFs. If it finds one, it deletes that document from the item and
        returns a Request to fetch that URL. We expect the callback to look for
        documents in this new page, add them to the item, and call us back with the
        resulting item. We'll repeat this process until all documents' URLs point
        to PDFs, then returning the unmodified item itself.
        '''
        for i, document in enumerate(item['documents']):
            for url in document['urls']:
                if not url.lower().endswith('.pdf'):
                    # This document is just a link to another page with more
                    # documents. As we'll parse this other page, we won't need it
                    # anymore.
                    del item['documents'][i]
                    return Request(
                        url,
                        meta={'item': item},
                        callback=self.parse_dap_page
                    )

        return item

    def parse_dap_page(self, res):
        '''
        Extracts the documents names and URLs from the Drug Approval Package
        pages. For documents that are split in multiple parts (e.g. some
        Medical Reviews), we merge them into a single document with each URL
        being added to the "urls" attribute in the order they appear on the
        page.
        '''
        def _get_document_name(el):
            selectors = ['::text', 'p::text', 'a::text']
            for selector in selectors:
                name = _clean_document_name(el.css(selector).extract_first())
                if name:
                    return name

        item = res.meta['item']

        for li in res.css('#user_provided > ul > li'):
            name = _get_document_name(li)
            urls = [_join_and_canonicalize_urls(res.url, url)
                    for url in li.css('a::attr(href)').extract()]
            item['documents'].append({'name': name, 'urls': urls})

        return self.expand_approval_history_documents(item)


def _join_and_canonicalize_urls(url1, url2):
    url = urlparse.urljoin(url1, url2)
    return canonicalize_url(url)


def _clean_document_name(name):
    result = name.replace('(PDF)', '') \
                 .replace('(s)', '')
    result = re.sub(r'\s{2,}', ' ', result)

    return result.strip()


def _response_cookies_to_dict(response):
    cookies = CookieJar().make_cookies(response, response.request)

    def _cookie_to_dict(cookie):
        return {
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
        }

    return [_cookie_to_dict(cookie) for cookie in cookies]


def _make_start_urls(prefix):
    initials = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0-9',
    ]
    return [prefix + initial for initial in initials]
