#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = "Henrik Finsberg"
SITENAME = "Henrik Finsberg's personal website"
SITEURL = ""

SITETITLE = "Henrik Finsberg"
SITESUBTITLE = "Senior Research Engineer"
SITEDESCRIPTION = "Foo Bar's Thoughts and Writings"
SITELOGO = SITEURL + "/images/profile.jpg"
FAVICON = SITEURL + "/images/favicon.ico"

HOME_TITLE = "Welcome to my personal website"
HOME_INDEX = """Hi, my name is Henrik Finsberg and this is my 
personal website. I am a applied mathematician who works as a 
researcher within the field of computational physiology.
"""

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

PATH = "content"
OUTPUT_PATH = "blog/"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
# HOME_HIDE_TAGS = False
DISABLE_URL_HASH = True


DISQUS_SITENAME = "henrikfinsberg.com"
# GOOGLE_ANALYTICS = "UA-1234-5678"
# GOOGLE_TAG_MANAGER = "GTM-ABCDEF"

# Blogroll
# LINKS = (("simula profile", "https://www.simula.no/people/henriknf"),)

# LINKS = (
#     ("Archives", "/archives.html"),
#     ("Categories", "/categories.html"),
#     ("Tags", "/tags.html"),
# )

# Social widget
SOCIAL = (
    ("envelope", "mailto:henriknf@simula.no"),
    ("github", "https://github.com/finsberg"),
    ("bitbucket", "https://bitbucket.org/finsberg/"),
    ("linkedin", "https://www.linkedin.com/in/henrik-finsberg-51664b53/"),
    ("researchgate", "https://www.researchgate.net/profile/Henrik_Finsberg"),
    ("simula", "https://www.simula.no/people/henriknf"),
)


DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR
DEFAULT_PAGINATION = 10

THEME = "themes/Flex-2.4.0"


DISQUS_SITENAME = "flex-pelican"
ADD_THIS_ID = "ra-55adbb025d4f7e55"

STATIC_PATHS = ["images", "assets"]


PLUGIN_PATHS = ["plugins"]
PLUGINS = ["jinja2content", "tipue_search"]

JINJA2CONTENT_PREFIX = "{% import 'macros.html' as m %}"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

GITHUB_CORNER_URL = "https://github.com/finsberg/finsberg.github.io"

USE_LESS = True
# USE_GOOGLE_FONTS = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
