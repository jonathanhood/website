#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jonathan'
SITENAME = u'jonathanhood.org'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

# Theme
THEME = 'pelican-simplegrey'
SINGLE_AUTHOR = True
DISPLAY_CATEGORIES_ON_MENU = False

# Setup filenames to extract dates and slugs
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ("LinkedIn", "http://www.linkedin.com/in/jonathanhood2"),
    ("Bitbucket", "http://bitbucket.org/jhood06")
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
