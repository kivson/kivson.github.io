#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kivson Andrade'
SITENAME = u"Kivson's Log"
SITEURL = 'http://localhost:8000'
DEFAULT_DATE = "fs"
PATH = 'content'

TIMEZONE = 'America/Cuiaba'

DEFAULT_LANG = u'pt'
DATE_FORMATS = {'pt': '%-d %b, %Y'}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
#  ('Pelican', 'http://getpelican.com/'),
#  ('Python.org', 'http://python.org/'),
#  ('Jinja2', 'http://jinja.pocoo.org/'),
#  ('You can modify those links in your config file', '#'),
#        )

# Social widget


SOCIAL = (
    ('github', 'https://github.com/kivson'),
    ('Twitter', 'https://twitter.com/kivson'),
    #('Linkedin', 'https://br.linkedin.com/pub/kivson-andrade/30/589/a78/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}




THEME = './themes/pelican-bootstrap3/'

PLUGIN_PATHS = ["plugins", "./plugins"]

#PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']



SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

TYPOGRIFY = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc',]

PYGMENTS_STYLE = 'monokai'

DISPLAY_CATEGORIES_ON_MENU = False
#BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_ARTICLE_INFO_ON_INDEX=True
DISPLAY_TAGS_INLINE=True
#SHOW_ARTICLE_AUTHOR =True
SHOW_ARTICLE_CATEGORY=True

CC_LICENSE = "CC-BY"

LOAD_CONTENT_CACHE = False
PLUGINS = ['sitemap', 'tipue_search',]
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

SITELOGO = "images/LOGO_BLOG.png"
SITELOGO_SIZE = "30"

#BOOTSTRAP_THEME = 'cosmo'

#LANDING_PAGE_ABOUT = {
#    "title": "Python, Web Crawling, IA, entre outros.",
#    "details":
#    "Sou Kivson Andrade, criei esse blog para compartilhar informações relacionados com "
#    "desenvolvimento. Minha linguagem favoria é Python. "
#    "Gosto de Linux, trabalho com Windows para viver. "
#    "Desenho e treino Kung-fu, leio ficção."
#
#}

#PROJECTS = [{
#                'name': 'SSaldo',
#                'url': 'https://play.google.com/store/apps/details?id=br.com.kivson.ssaldo',
#                'description':  'Aplicativo para exibir saldo e extrato de cartões alimentação e refeição. '
#                                'Extrai os dados de um site usando um leitor de captcha.'},
#            #{'name': 'Elegant Theme for Pelican',
#            #'url': 'http://oncrashreboot.com/pelican-elegant',
#            #'description': 'A clean and distraction free theme, with search and a'
#            #' lot more unique features, using Jinja2 and Bootstrap'},
#]