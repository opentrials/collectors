# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base


# Module API

def extract_data(sel, gpath, kpath, vpath):
    data = []
    group = None
    name = None
    value = None
    for sel in sel.css('%s, %s, %s' % (gpath, kpath, vpath)):
        text = extract_text(sel)
        if sel.css(gpath):
            group = text
        elif sel.css(kpath):
            name = base.utils.slugify(text)
        else:
            value = text
            if name and value:
                data.append((group, name, value))
            name = None
            value = None
    return data


def extract_text(sel):
    text = ''
    texts = sel.xpath('.//text()').extract()
    if texts:
        text = ' '.join(texts).strip()
    return text
