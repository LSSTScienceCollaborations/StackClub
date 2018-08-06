import sys
import os
import sphinx_rtd_theme

# Provide path to the python modules we want to run autodoc on
sys.path.insert(0, os.path.abspath('../stackclub'))
# Avoid imports that may be unsatisfied when running sphinx, see:
# http://stackoverflow.com/questions/15889621/sphinx-how-to-exclude-imports-in-automodule#15912502
autodoc_mock_imports = ["urllib", "urllib.request", "request", "nbformat", "IPython", "IPython.core.interactiveshell"]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode' ]

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

master_doc = 'index'
autosummary_generate = True
autoclass_content = "class"
autodoc_default_flags = ["members", "no-special-members"]

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }

project = u'StackClub'
author = u'The LSST Science Collaborations'
copyright = u'2018, ' + author
version = "0.1"
release = "0.1.0"