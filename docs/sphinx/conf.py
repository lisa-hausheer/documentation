# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import logging as pylogging
import os
import sys

from sphinx.util import logging


sys.path.insert(0, os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = "documentation"
copyright = "2021, lhausheer@meilleursagents.com"
author = "lhausheer@meilleursagents.com"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "recommonmark",
]

# Link to other documentation
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "statsmodels": ("https://www.statsmodels.org/stable/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

nitpick_ignore = [
    ("py:class", "sqlalchemy.ext.declarative.declarative_base"),
    ("py:class", "ma_models.mixins.BaseMixin"),
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_logo = "_static/logo_ma.svg"

html_theme_options = {
    "external_links": [
        # {"url": "https://pandas.pydata.org/pandas-docs/stable/", "name": "Pandas Docs"}  # noqa: E501
    ],
    "github_url": "https://github.com/lisa-hausheer/documentation",
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "lisa-hausheer",
    "github_repo": "EncartaExport",
    "github_version": "master",
    "doc_path": "docs",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# Workaround for https://github.com/agronholm/sphinx-autodoc-typehints/issues/123
# When this https://github.com/agronholm/sphinx-autodoc-typehints/pull/153
# gets merged, we can remove this
class FilterForIssue123(pylogging.Filter):
    def filter(self, record: pylogging.LogRecord) -> bool:
        # You probably should make this check more specific by checking
        # that dataclass name is in the message, so that you don't filter out
        # other meaningful warnings
        return not record.getMessage().startswith("Cannot treat a function")


logging.getLogger("sphinx_autodoc_typehints").logger.addFilter(FilterForIssue123())
# End of a workaround
