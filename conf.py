# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import subprocess, sys, os, json
from pathlib import Path

# Get git information
try:
    output = subprocess.check_output(["git ls-remote --get-url origin"], shell=True).decode(sys.stdout.encoding)
    parts = str(output).split(".com/")[1].split("/")
    github_repo = parts[1].split(".git")[0]
    github_user = parts[0]
    github_version = str(subprocess.check_output(["git rev-parse --abbrev-ref HEAD"], shell=True).decode(sys.stdout.encoding)).strip() + "/"
except Exception as e:
    print("Could not get git information: " + str(e))
    github_repo = "mirte-workshops"
    github_user = "mirte-robot"
    github_version = "main"
# -- Project information -----------------------------------------------------

project = 'Mirte Workshops'
copyright = 'Delft University of Technology, CC BY-SA 4.0'
articles_settings = json.loads(open('_static/js/articles.json').read())

lang = articles_settings["default_language"]  # default language
lang_long = ""
for lang_opt in articles_settings["languages"]:
    print("Checking for lang: " + str(lang_opt))
    # print(tags.tags)
    if f'lang_{lang_opt["short"]}' in tags:
        lang = lang_opt["short"]
        lang_long = lang_opt["long"]
        print(f"Found lang: {lang}")
    if(lang_opt["short"] == articles_settings["default_language"]):
        lang_default = lang_opt["short"]
        lang_default_long = lang_opt["long"]

try:
    with open(f'modules/banners/banner.{lang}.rst') as f:
        banner_text = f.read()
except:
    print(f"No banner found for {lang}, this is required")

def getArticles():
    articles = []
    for dirpath, dirnames, filenames in os.walk('.', followlinks=True):
        for filename in filenames:
            if filename.endswith('.rst'):
                full_path = os.path.join(dirpath, filename)
                if os.path.normpath(full_path) != os.path.normpath('./index.rst') and full_path.count(".") == 3:
                    articles.append(full_path[2:-7])
    unique_articles = list(set(articles))
    return unique_articles

# For multi-lang, copy article.{lang}.rst to article.rst
def copyArticles(articles):
    for article in articles:
        try:
            # check if file exists
            translated_file = f'{article}.{lang}.rst'
            put_warning = False
            if(not os.path.exists(translated_file)):
                print(f"missing article file for {article} in {lang}") # TODO: add banner
                translated_file = f'{article}.{lang_default}.rst'
                put_warning = True
            
            with open(translated_file) as f_lang:
                with open(f'{article}.rst', 'w') as f_dest:
                    article_content = f_lang.read()
                    if(put_warning):
                        if(not ".. WARNING_SPOT" in article_content):
                            print("missing WARNING_SPOT place in " + article)
                        else:
                            article_content = article_content.replace(".. WARNING_SPOT\n", banner_text.replace("{github_user}", github_user).replace("{github_repo}", github_repo))
                    f_dest.write(article_content)
        except Exception as e:
            print(e)
            print("missing article file for " + article)



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.video', 'sphinx_design']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# don't build the original language files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_modules', 'docs-env', *[f'**/*.{x["short"]}.rst' for x in articles_settings["languages"]], 'docs/banners/*', 'docs/index/*' ]


# intl
# locale_dirs = glob.glob('./docs/*/_locale/')
# locale_dirs.append('locale/')
# print(locale_dirs)
gettext_compact = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
author = 'MIRTE team'
html_theme = 'sphinx_book_theme'
html_title = "Mirte Workshops"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = ['js/custom.js', 'js/matomo.js']

html_css_files = [
      "css/custom.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css",
]

html_favicon = "_static/favicon.png"

## For Book Theme
html_context = {
   "github_repo": "mirte-workshops",
   "github_user": "mirte-robot"
}

html_sidebars = {
    "**": ["navbar-logo.html", "sbt-sidebar-nav.html"]
}


# Try to update from git
try:
    output = subprocess.check_output(["git ls-remote --get-url origin"], shell=True).decode(sys.stdout.encoding)
    parts = str(output).split(".com/")[1].split("/")
    html_context["github_repo"] = github_repo
    html_context["github_user"] = github_user
    html_context['github_version'] = github_version
except Exception as e:
    print("Could not get git information: " + str(e))

html_theme_options = {
    "use_download_button": False,
    "repository_url": f'https://github.com/{html_context["github_user"]}/{html_context["github_repo"]}',
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": False,
    "secondary_sidebar_items": [],
    "extra_footer": "<a href='https://mirte.org/privacy'>privacy</a>",
}


linkcheck_ignore = [r'^http://$', r'^http://mirte.local.*', r'.*localhost.*', r'.*192.168.4.*']
linkcheck_anchors_ignore_for_url = [

]
language = lang

def remove_copied_files(app, exception):
    for file in app.articles:
        path = Path(f"{file}.rst")
        if path.exists():
            path.unlink()


def setup(app):
    app.articles = getArticles()
    copyArticles(app.articles)
    app.connect('build-finished', remove_copied_files)

