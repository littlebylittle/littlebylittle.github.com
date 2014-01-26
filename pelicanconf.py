#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Parasite'
SITENAME = u"Parasite's Thoughts"
SITEURL = '/output'
#SITEURL = ''

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
	  ('Home', '/'), )

#IMG author
AUTHOR_IMG = 'http://liubavyshka.ru/_ph/36/2/813597786.gif'
# Social widget
SOCIAL = (('My github', 'https://github.com/littlebylittle/#'), )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Enable get date from file:
DEFAULT_DATE = 'fs'

#using theme for blog
THEME = 'pelican-themes/jesuislibre'

