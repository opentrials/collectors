# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Json, Array


# Module API

class Record(base.Record):

    # Config

    table = 'pubmed'

    # Medline

    pmid = Text(primary_key=True)
    date_created = Date('%Y-%m-%d')
    date_completed = Date('%Y-%m-%d')
    date_revised = Date('%Y-%m-%d')
    country = Text()
    medline_ta = Text()
    nlm_unique_id = Text()
    issn_linking = Text()
    mesh_headings = Json()

    # Journal

    journal_issn = Text()
    journal_title = Text()
    journal_iso = Text()

    # Article

    article_title = Text()
    article_abstract = Text()
    article_authors = Array()
    article_language = Text()
    article_publication_type_list = Array()
    article_vernacular_title = Text()
    article_date = Date('%Y-%m-%d')

    # Pubmed

    publication_status = Text()
    article_ids = Json()
    registry_ids = Json()
