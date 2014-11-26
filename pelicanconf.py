#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kivson Andrade'
SITENAME = u'blog.kivson'
SITEURL = 'http://localhost:8000/'

PATH = 'content'

TIMEZONE = 'America/Cuiaba'

DEFAULT_LANG = u'pt'
DATE_FORMATS = {'pt': '%b %d, %Y'}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
# ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget


SOCIAL = (
    ('github', 'https://github.com/kivson', 'github'),
    ('Twitter', 'https://twitter.com/kivson', 'twitter'),
    #('Linkedin', 'https://br.linkedin.com/pub/kivson-andrade/30/589/a78/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True




THEME = './themes/pelican-elegant-master/'

PLUGIN_PATHS = ["plugins", "./plugins"]
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

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

LANDING_PAGE_ABOUT = {
    "title": "Programação, Python, Web Crawling, IA, entre outros.",
    "details":
    "Sou Kivson Andrade, criei esse blog para compartilhar informações relacionados com "
    "desenvolvimento. Minha linguagem favoria é Python. "
    "Gosto de Linux, trabalho com Windows para viver. "
    "Desenho e treino Kung-fu, leio ficção."

}

PROJECTS = [{
                'name': 'SSaldo',
                'url': 'https://play.google.com/store/apps/details?id=br.com.kivson.ssaldo',
                'description':  'Aplicativo para exibir saldo e extrato de cartões alimentação e refeição. '
                                'Extrai os dados de um site usando um leitor de captcha.'},
            #{'name': 'Elegant Theme for Pelican',
            #'url': 'http://oncrashreboot.com/pelican-elegant',
            #'description': 'A clean and distraction free theme, with search and a'
            #' lot more unique features, using Jinja2 and Bootstrap'},
]