#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
from datetime import date

AUTHOR = 'Austin "Paco" Rainwater'
SITENAME = 'paco, wtf'
SITEURL = 'https://paco.wtf'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

CLICKY_CODE = 101328548
BUILD_DATE = date.today()
THEME = 'themes/wtf'
DEFAULT_DATE = 'fs'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""