# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

## THINGS TO CONFIGURE
## ---------------------------------------------------------------------

AUTHOR = u'AmazonOfertas25'
SITENAME = u'Ofertas que te dejarán sentado!'
SITESUBTITLE = u'Las ofertas del canal @amazonofertas25 en Telegram'
SITEURL = u'/'
DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'ofertas'
CLAIM_GOOGLE = "7QrCnaeuK3HPjHwmZ4DWrwgo5ySpPLwJE2ZTFvrNGeI"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"


LANDING_PAGE_ABOUT = {}


PROJECTS = [{'name': 'AmazonOfertas25', 'url': 'https://t.me/AmazonOfertas25',              'description': 'Ofertas con un 25% de descuento!'}, {'name':"Bebé",'url':  "https://t.me/estodobebe"}, {'name':"Moda",'url':  "https://t.me/estodomoda"}, {'name':"Tecnología",'url':  "https://t.me/todotech"}, {'name':"Domótica",'url':  "https://t.me/estododomotica"}, {'name':"Lego", 'url': "https://t.me/brickchollo"}, {'name':"Playmobil", 'url': "https://t.me/joinchat/AAAAAE3WwL-YCJ5wuLLNhA"}, {'name':"Juguetes",'url':  "https://t.me/estodojuguetes"}, {'name':"Ofertas con 50% o más de descuento",'url':  "https://t.me/joinchat/AAAAAFSZXxC24V2PeMtTSg"}, {'name':"Funko", 'url': "https://t.me/joinchat/AAAAAFA1UfRMI0CV8ZsZuw"}, {'name':"Todas las ofertas",'url':  "https://t.me/amazonfertas"}]


LINKS = (('Redken on telegram', 'https://t.me/redken_bot'))

# Keep 'name' like 'twitter' with what 'FontAwesome has for putting the right icon'

SOCIAL = ()


# TWITTER_USERNAME = "fillit"
# Update if you use amazon links
# AMAZON_ONELINK = "23824450-ef77-4537-9259-8590465886f1"

AMAZON_BESTAZON = """var BestAzon_Configuration = {
"Amzn_AfiliateID_US": "redken01-20",
"Amzn_AfiliateID_CA": "redken03-20",
"Amzn_AfiliateID_GB": "redken01-21",
"Amzn_AfiliateID_DE": "redken02-21",
"Amzn_AfiliateID_FR": "redken07-21",
"Amzn_AfiliateID_ES": "redken-21",
"Amzn_AfiliateID_IT": "redken0d-21",
"Amzn_AfiliateID_JP": "",
"Amzn_AfiliateID_IN": "",
"Amzn_AfiliateID_CN": "",
"Amzn_AfiliateID_MX": "",
"Amzn_AfiliateID_BR": "",
"Conf_Custom_Class": " BestAzon_Amazon_Link ", //enter if you'll like to add any CSS class to the Amazon links (can be used for styling)
"Conf_New_Window": "1", //enter "1" if you'll like to open Amazon links in new window (recommended), "2" to force open in the same window, keep blank if you'd use the defaults
"Conf_Link_Follow": "1", //enter "1" if you'll like to add no-follow to the Amazon links (recommended), "2" to not add no-follow
"Conf_Product_Link": "1", //enter "1" if you'll like to redirect international visitors to equivalent search page on local Amazon stores (recommended and fast), "2" if you want them to go to equiavalent product page (slow)
"Conf_Tracking": "1", //enter "1" if you'll like to enable tracking (useful to optimize the service to you), "2" to disable
"Conf_Footer": "1", //enter "1" to add credit in footer (recommended), "2" to disable
"Conf_Link_Keywords": "", //enter additional keywords - if any of these keywords is found in any URL on your site, that will be sent to Bestazon for localization (useful if you use short links like bitly to hide your affiliate links). E.g. enter "/amazon/" if all your Amazon links containt the string /amazon/
"Conf_Hide_Redirect_Link": "1", //enter "1" to not replace your original link with bestazon links (recommended), "2" if you want to replace (not recommended)
"Conf_Source": "BestAzonScript" //DO NOT CHANGE THIS
};
"""

# GOOGLE_ANALYTICS tracking ID
# GOOGLE_ANALYTICS = "UA-81705-12"

## Configure if you use Disqus for comments
# DISQUS_SITENAME = "iranzo-github-io"
# DISQUS_DISPLAY_COUNTS = True


# Extra files customization
# Extra files customization
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}


EXTRA_TEMPLATES_PATHS = [
    "plugins/revealmd/templates",  # eg: "plugins/revealmd/templates"
]

STATIC_PATHS = [ 'images' , 'extra' ]


## ONLY TOUCH IF YOU KNOW WHAT YOU'RE DOING!
## ---------------------------------------------------------------------

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

# Put as draft content in the future
WITH_FUTURE_DATES = False

# Put full text in RSS feed
RSS_FEED_SUMMARY_ONLY = False

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss'

CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss'
TRANSLATION_FEED_ATOM = 'feeds/{lang}.atom.xml'
TRANSLATION_FEED_RSS = 'feeds/{lang}.rss'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss'
TAG_FEED_ATOM = 'feeds/tag_{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/tag_{slug}.rss'

DISPLAY_PAGES_ON_MENU = True

CACHE_CONTENT = False
CACHE_PATH = '.cache'
LOAD_CONTENT_CACHE = False

# Plugins
PLUGIN_PATHS = ['plugins']

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'render_math', 'share_post',
           'series', 'assets', 'post_stats', 'revealmd']

           # 'better_codeblock_line_numbering'
           # 'better_figures_and_images'

THEME = 'themes/elegant'

#elegant
TYPOGRIFY = True
RECENT_ARTICLE_SUMMARY = True
RESPONSIVE_IMAGES = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': True
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u''

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
USE_FOLDER_AS_CATEGORY = False

SEARCH_BOX = False

# URL Settings to be compatible with octopress
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'

YEAR_ARCHIVE_URL = 'blog/archive/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'blog/archive/{date:%Y}/index.html'

MONTH_ARCHIVE_URL = 'blog/archive/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = 'blog/archive/{date:%Y}/{date:%m}/index.html'

CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'

TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

ARCHIVES_URL = 'blog/archives/'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

CATEGORIES_URL = 'blog/categories/'
CATEGORIES_SAVE_AS = 'blog/categories/index.html'

TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'

TAGS_URL = 'tags'
TAGS_SAVE_AS = ''
AUTHORS_URL = 'authors'
AUTHORS_SAVE_AS = ''
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = ''
ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = ''

DEFAULT_PAGINATION = 30
DEFAULT_ORPHANS = 0

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# sitemap
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

SITE_UPDATED = datetime.date.today()

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
