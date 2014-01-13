#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Sample Author"
SITENAME = u"My Sample Blog"
SITESUBTITLE = u"Blogs, Blags, and Blagollas"
# Uncomment the follow to add a "About the Author" section to the navigation pane:
AUTHOR_ABOUT = u'I\'m  Sample Author. You may remember me from such example git repos as ...'
TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 3

# By default we enable pretty highlighing in markdown:
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'toc']

# Leave this blank for local development, publishconf.py has the "real" value:
SITEURL = ''

DISPLAY_CATEGORIES_ON_MENU = False

FEED_ATOM = ''
FEED_RSS = ''
#FEED_DOMAIN = SITEURL
#CATEGORY_FEED_RSS = 'feeds/category.%s.rss'
#TAG_FEED_RSS = None
#FEED_MAX_ITEMS = 30

# Static files
# Uncomment and set to the filename of your favicon:
#FAVICON_FILENAME = 'favicon.ico'

# Any extra files should be added here
STATIC_PATHS = [
    'extras',
    'images'
    ]
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/publickey.asc': {'path': 'publickey.asc'}
    }

# Here's a sample EXTRA_PATH_METADATA that adds the favicon, an iOS touch icon and a GPG key:
#EXTRA_PATH_METADATA = {
#    'extras/robots.txt': {'path': 'robots.txt'},
#    'extras/favicon.ico': {'path': 'favicon.ico'},
#    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
#    'extras/publickey.asc': {'path': 'publickey.asc'}
#    }


#Theme
# Defaults to using the octopress theme for pelican:
THEME = './themes/octopress'
SINGLE_AUTHOR = False
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_DATE_FORMAT = ('%b %d %Y')
#TYPOGRIFY = True

# Blogroll (additional links to display)
#LINKS = (
#    ('GitHub', 'https://github.com/sample-user-on-github'),
#    ('Example', 'http://www.example.com/'),
#)


# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Cleaner Articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

