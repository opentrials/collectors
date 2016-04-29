# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from . import utils
from .parser import PubmedParser


# Module API

class PubmedSpider(base.Spider):

    # Public

    name = 'pubmed'
    allowed_domains = ['eutils.ncbi.nlm.nih.gov']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create parser
        self.parser = PubmedParser()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/',
                template='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id={pmid}&retmode=xml',
                date_from=date_from, date_to=date_to)

        # Set parser
        self.parse = self.parser.parse

        # Inherit parent
        super(PubmedSpider, self).__init__(*args, **kwargs)
