"""Flask configuration"""

# Debug mode
DEBUG = True

# Flask-FlatPages settings
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'tables', 'fenced_code', 'footnotes']

# Frozen-Flask settings
FREEZER_DESTINATION = 'build'
FREEZER_RELATIVE_URLS = True
FREEZER_REMOVE_EXTRA_FILES = True

# Site settings
SITE_TITLE = "Jacob Gottesman | Data Scientist"
SITE_DESCRIPTION = "Portfolio of Jacob Gottesman, Data Scientist specializing in machine learning, NLP, and statistical modeling."
GITHUB_URL = "https://github.com/jacobgottesman"
LINKEDIN_URL = "https://www.linkedin.com/in/jacob-gottesman-neu"
EMAIL = "jacobgottesman1@gmail.com"
PHONE = "(267) 565-8065"
LOCATION = "Boston, MA"