#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colton Myers'
SITENAME = u'Me, Myself, and Colton'
SITEURL = 'http://localhost:8000'

# Change to False if there are caching issues
LOAD_CONTENT_CACHE = True

STATIC_PATHS = ['images', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'}
}

THEME = 'themes/pelican-octopress-theme'
SITESUBTITLE = 'Leading to a rapid loss of interest since 2011'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>'
DISPLAY_CATEGORIES_ON_MENU = False
SINGLE_AUTHOR = True
MINT = False
GOOGLE_ANALYTICS = 'UA-57037100-1'

DISQUS_SITENAME = 'blog-cmyers-net'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE_FORMAT = '%b %d %Y'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (
        ('RSS', 'http://blog.cmyers.net/rss.xml'),
        ('Twitter', 'http://twitter.com/basepi'),
        ('Tech Blog', 'http://blog.basepi.net'),
)

TWITTER_USERNAME = 'basepi'
TWITTER_USER = 'basepi'

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
