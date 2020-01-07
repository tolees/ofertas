# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

## THINGS TO CONFIGURE
## ---------------------------------------------------------------------

AUTHOR = "AmazonOfertas25"
SITENAME = "Ofertas del día en Amazon que te dejarán helado!"
SITESUBTITLE = "Las ofertas del canal @amazonofertas25 y amigos en Telegram"
SITEURL = "/"
DEFAULT_LANG = "es"
DEFAULT_CATEGORY = "ofertas"
CLAIM_GOOGLE = "7QrCnaeuK3HPjHwmZ4DWrwgo5ySpPLwJE2ZTFvrNGeI"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"


LANDING_PAGE_ABOUT = {}

PROJECTS_TITLE = "Nuestros canales de ofertas"

PROJECTS = [
    {"name": "💻Es Todo Tecnología", "url": "https://t.me/todotech"},
    {"name": "🧱Brickchollo (Lego)", "url": "https://t.me/brickchollo"},
    {"name": "🎎Es todo playmobil", "url": "https://t.me/estodoplaymobil"},
    {"name": "👶Es todo bebé", "url": "https://t.me/estodobebe"},
    {"name": "🤯Es todo funko", "url": "https://t.me/estodofunko"},
    {"name": "🏠Es todo domotica", "url": "https://t.me/estododomotica"},
    {"name": "👚Es todo moda", "url": "https://t.me/estodomoda"},
    {"name": "🧸Es todo juguetes", "url": "https://t.me/estodojuguetes"},
    {"name": "🍏Es todo Apple", "url": "https://t.me/estodoapple"},
    {"name": "📊Mínimos históricos", "url": "https://t.me/minimos_historicos"},
    {"name": "Lego Deals", "url": "https://t.me/legoue"},
    {"name": "🛍Ofertas 25% o más", "url": "https://t.me/ofertas25"},
    {
        "name": "🛍Ofertas 50% o más",
        "url": "https://t.me/ofertas50",
    },
    {
        "name": "🛍Ofertas 70% o más",
        "url": "https://t.me/ofertas70",
    },
    {"name": "🧱Lego Investor", "url": "https://t.me/legoinvestor"},
    {"name": "📏La vuelta al cole", "url": "https://t.me/vueltaalcole"},
    {"name": "🎅🎄🤶🎁 Navidad", "url": "https://t.me/esnavidad"},
    {"name": "🇬🇧UK Deals", "url": "https://t.me/allukdeals"},
    {"name": "🇮🇹Italia dsconti", "url": "https://t.me/dsconti"},
    {"name": "🇫🇷France Soldes", "url": "https://t.me/soldeszone"},
    {"name": "🇩🇪Germany Rabbate", "url": "https://t.me/skontozone"},
    {"name": "Shurchollo", "url": "https://t.me/shurchollo"},
    {"name": "Ofertachollos", "url": "https://t.me/ofertachollos"},
    {
        "name": "Black Friday & Cyber Monday",
        "url": "https://t.me/blackfriday_cybermonday",
    },
    {"name": "👪Sylvanian Families", "url": "https://t.me/sylvanian_families"},
    {"name": "🤑Errores de precio", "url": "https://t.me/errores_de_precio"},
]


LINKS = ("Descuenbot on telegram", "https://t.me/descuenbot")

# Keep 'name'like 'twitter'with what 'FontAwesome has for putting the right icon'

SOCIAL = ()


# TWITTER_USERNAME = "fillit"
# Update if you use amazon links
# AMAZON_ONELINK = "23824450-ef77-4537-9259-8590465886f1"

AMAZON_BESTAZON = """var BestAzon_Configuration = {
"Amzn_AfiliateID_US": "redken00-20",
"Amzn_AfiliateID_CA": "redken05-20",
"Amzn_AfiliateID_GB": "redken01-21",
"Amzn_AfiliateID_DE": "redken02-21",
"Amzn_AfiliateID_FR": "redken0c-21",
"Amzn_AfiliateID_ES": "redken-21",
"Amzn_AfiliateID_IT": "redken015-21",
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
GOOGLE_ANALYTICS = "UA-81705-17"

## Configure if you use Disqus for comments
# DISQUS_SITENAME = "iranzo-github-io"
# DISQUS_DISPLAY_COUNTS = True


# Extra files customization
# Extra files customization
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}


EXTRA_TEMPLATES_PATHS = [
    "plugins/revealmd/templates",  # eg: "plugins/revealmd/templates"
]

STATIC_PATHS = ["images", "extra"]


## ONLY TOUCH IF YOU KNOW WHAT YOU'RE DOING!
## ---------------------------------------------------------------------

PATH = "content"

TIMEZONE = "Europe/Madrid"

# Put as draft content in the future
WITH_FUTURE_DATES = False

# Put full text in RSS feed
RSS_FEED_SUMMARY_ONLY = False

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = ""
FEED_ALL_RSS = ""

CATEGORY_FEED_ATOM = ""
CATEGORY_FEED_RSS = ""
TRANSLATION_FEED_ATOM = ""
TRANSLATION_FEED_RSS = ""
AUTHOR_FEED_ATOM = ""
AUTHOR_FEED_RSS = ""
TAG_FEED_ATOM = ""
TAG_FEED_RSS = ""

DISPLAY_PAGES_ON_MENU = True

CACHE_CONTENT = False
CACHE_PATH = ".cache"
LOAD_CONTENT_CACHE = False

# Plugins
PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    "sitemap",
    "extract_toc",
    "tipue_search",
    "liquid_tags.img",
    "render_math",
    "share_post",
    "series",
    "assets",
    "post_stats",
    "revealmd",
]

# 'better_codeblock_line_numbering'
# 'better_figures_and_images'

THEME = "themes/elegant"

# elegant
TYPOGRIFY = True
RECENT_ARTICLE_SUMMARY = True
RESPONSIVE_IMAGES = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": "true"},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = ""

FILENAME_METADATA = "(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = False

SEARCH_BOX = False

# URL Settings to be compatible with octopress
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

ARTICLE_LANG_URL = "{slug}-{lang}/"
ARTICLE_LANG_SAVE_AS = "{slug}-{lang}/index.html"

YEAR_ARCHIVE_URL = "archive/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "archive/{date:%Y}/index.html"

MONTH_ARCHIVE_URL = "archive/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "archive/{date:%Y}/{date:%m}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"

CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"

TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"

TAGS_URL = "tags"
TAGS_SAVE_AS = ""
AUTHORS_URL = "authors"
AUTHORS_SAVE_AS = ""
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = ""
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = ""

DEFAULT_PAGINATION = 30
DEFAULT_ORPHANS = 0

PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

SITE_UPDATED = datetime.date.today()

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ("Tags", TAGS_URL, TAGS_SAVE_AS),
    ("Archives", ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
