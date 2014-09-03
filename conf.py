# .. -*- coding: utf-8 -*-
#
#    Copyright (C) 2012-2013 Bryan A. Jones.
#
#    This file is part of CodeChat.
#
#    CodeChat is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#    CodeChat is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with CodeChat.  If not, see <http://www.gnu.org/licenses/>.
#
# **************************************************
# conf.py - Sphinx configuration for use by CodeChat
# **************************************************
# This file supplies configuration information for Sphinx, which CodeChat uses to produces its documentation. It was originally created by sphinx-quickstart.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# Use the CodeChat version date in its generated documentation.
import CodeChat
#
# General configuration
# =====================
# Add any `Sphinx extension module names <http://sphinx-doc.org/extensions.html>`_ here, as strings. They can be extensions coming with Sphinx (named ``sphinx.ext.*``) or your custom ones. **NOTE:** CodeChat relies on the ``CodeChat.CodeToRestSphinx`` extension; this must be present in every CodeChat project.
extensions = ['CodeChat.CodeToRestSphinx', 'sphinx.ext.graphviz']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
##source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'CodeChat'
copyright = u'2014, Bryan A. Jones'

# The version info for the project you're documenting, which acts as replacement for |version| and |release|, and is also used in various other places throughout the built documents.
#
# The short X.Y version.
version = CodeChat.__version__
# The full version, including alpha/beta/rc tags. For simplicity, use the same string.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation for a list of supported languages.
##language = None

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = ['build',
                    'dist',
                    '_build',
                    'tre-0.8.0-src',
                    'CodeChat/example',
                    'CodeChat/CodeChat_ui.py',
                    ]

# The reST default role (used for this markup: `text`) to use for all documents.
##default_role = None

# The default language to highlight source code in. The default is 'python'.
# The value should be a valid Pygments lexer name, see
# Showing code examples for more details.
highlight_language = 'python3'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, keep warnings as ?system message? paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
keep_warnings = True
#
# Options for HTML output
# =======================
# The theme to use for HTML and HTML Help pages.  CodeChat can ONLY use this theme, which was hand-modified to deal with limitations (no CSS include support) of the Qt QTextBrowser.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme further.  For a list of options available for each theme, see the documentation. CodeChat's QTextBrowser gets confused by the sidebar, so turn it off.
html_theme_options = { "nosidebar" : "true" }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['default.css']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If false, no module index is generated.
html_domain_indices = False
