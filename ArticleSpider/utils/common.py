#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ye Junyu'

import hashlib

def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


