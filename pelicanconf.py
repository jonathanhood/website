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
NUM_FULL_ARTICLES = 4
NUM_LINKED_ARTICLES = 7

# Setup filenames to extract dates and slugs
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("Github", "https://github.com/jonathanhood"),
    ("Twitter", "https://twitter.com/jonathan_hood"),
    ("Facebook", "https://www.facebook.com/jonathanhood.hsv"),
    ("LinkedIn", "http://www.linkedin.com/in/jonathanhood2"),
)

# Static Folders
STATIC_PATHS = [
    'images',
    'static'
]

# Files to manually place
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
}
# Pagination 
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
