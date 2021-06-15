#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) Bouvet ASA - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

import os
import sys

import cornice
import guzzle_sphinx_theme

import pathlib
import shutil

def split_rst_file_root_level(root_level_header, files, output_folder, rename_ref_prefix):
    """
    I use the functions within me to split RST files into a file for each
    root level header in the file.
    """

    def find_root_headers(file):
        """
        I'm a function which finds all the root level headers in a document.
        Root level header character can be set at the top variable.
        """
        lines = open(file).readlines()
        cur_ref = None
        tmp_cur_ref = None
        prev_line = None
        returnlist = []
        for l in lines:
            l = l.replace('\n', '')
            if l.startswith('.. _') and l.endswith(':'):
                tmp_cur_ref = l
            linelength = len(l)
            reflength = 0
            for c in l:
                if c == root_level_header:
                    reflength += 1
            if linelength == reflength and linelength != 0:
                cur_ref = tmp_cur_ref
                returnlist.append({
                    "reference": cur_ref,
                    "title": prev_line
                })
                #print(f'#\n{cur_ref}\n\n{prev_line}\n{l}\n#')
            prev_line = l


        return returnlist

    def createFiles(file, splitonthis: list):
        """
        I'm a function which a splits a string on a list of strings.
        I make sure that there is no overlap in the output strings.
        """
        mainfile = open(file).read()
        createfiles = []
        splitonthis.reverse()
        for x, e in enumerate(splitonthis):
            splitted_main_file = mainfile.split(e['reference'])
            ref_name = f".. _{rename_ref_prefix}{e['reference'][4:]}"
            createfiles.append(ref_name + splitted_main_file[-1])
            createfiles.append(ref_name + splitted_main_file[-1])
            if splitted_main_file:
                mainfile = splitted_main_file[0]
        createfiles.reverse()
        return createfiles

    def writeFiles(writingFiles: list, file_prefix):
        """
        I'm a simple function which writes a rst files.
        I create a file named after the first line for each file provided.
        I suffix the filename with '.rst'
        I also remove the top line from the file so that there won't be
        duplicate references.
        """
        for wf in writingFiles:
            filename = wf.split('\n')[0][4:-1] + '.rst'
            curfile = open(f'{output_folder}/{file_prefix}{filename}', 'w')
            print(f'output_folder : {output_folder}\nfile_prefix : {file_prefix}\nfilename : {filename}')
            wf = wf.replace(f'./media/', f'/training/{filenameSplitted[0]}/media/')
            wf = wf.replace('.. _', '..\n  .. _')
            wf = ':orphan:\n\n' + wf
            curfile.write(wf)
            curfile.close()

    fullpath = os.path.join(pathlib.Path().absolute(), output_folder)
    if os.path.exists(fullpath):
        shutil.rmtree(fullpath)
    os.makedirs(fullpath)
    for f in files:
        filenameSplitted = f.split('/')[-2:]
        file_prefix = f'{filenameSplitted[0][4:]}_{filenameSplitted[1][4:-4]}_'
        print(file_prefix)
        splitonthis = find_root_headers(f)
        file = open(f).read()
        writeFiles(createFiles(file=f, splitonthis=splitonthis), file_prefix=file_prefix)

files = ["training/010_architecture_and_concepts/020_Beginner.rst","training/010_architecture_and_concepts/030_Novice.rst","training/010_architecture_and_concepts/040_Intermediate.rst","training/010_architecture_and_concepts/050_Advanced.rst","training/010_architecture_and_concepts/060_Epilogue.rst","training/010_architecture_and_concepts/architecture_and_concepts.rst","training/020_systems/020_Beginner.rst","training/020_systems/030_Novice.rst","training/020_systems/040_Intermediate.rst","training/020_systems/060_Epilogue.rst","training/020_systems/systems.rst","training/030_dtl/020_Beginner.rst","training/030_dtl/030_Novice.rst","training/030_dtl/040_Intermediate.rst","training/030_dtl/050_Advanced.rst","training/030_dtl/060_Epilogue.rst","training/030_dtl/dtl.rst","training/040_projects_and_infrastructure/020_Beginner.rst","training/040_projects_and_infrastructure/030_Novice.rst","training/040_projects_and_infrastructure/040_Intermediate.rst","training/040_projects_and_infrastructure/060_Epilogue.rst","training/040_projects_and_infrastructure/projects_and_infrastructure.rst","training/050_microservices/020_Beginner.rst","training/050_microservices/030_Novice.rst","training/050_microservices/040_Intermediate.rst","training/050_microservices/050_Advanced.rst","training/050_microservices/060_Epilogue.rst","training/050_microservices/microservices.rst","training/060_sesam_in_the_wild/020_Beginner.rst","training/060_sesam_in_the_wild/030_Novice.rst","training/060_sesam_in_the_wild/040_Intermediate.rst","training/060_sesam_in_the_wild/050_Advanced.rst","training/060_sesam_in_the_wild/060_Epilogue.rst","training/060_sesam_in_the_wild/sesam_in_the_wild.rst"]
output_folder = 'training/courses/tmp'
root_level_header = '~'
rename_ref_prefix = 'tc_'
split_rst_file_root_level(root_level_header, files, output_folder, rename_ref_prefix)


# import sphinx_rtd_theme


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute.
sys.path.insert(0, os.path.abspath(cornice.__file__))

# Add the sesamclient to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../client")))

import pprint
print ("sys.path:%s" % pprint.pformat(sys.path))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxarg.ext',
              'sphinxcontrib.openapi'
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Sesam'
copyright = '2021 Sesam.io AS'
author = 'The Sesam Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'x.y'
# The full version, including alpha/beta/rc tags.
release = 'who cares'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', os.path.basename(os.environ['VIRTUAL_ENV']), 'git.rst', 'project-setup.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'
# html_theme = "sphinx_rtd_theme"

# Adds an HTML table visitor to apply Bootstrap table classes
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
   # Set the name of the project to appear in the sidebar
   "project_nav_name": "Sesam",
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Sesam documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Sesamdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'Sesam.tex', 'Sesam Documentation',
   'Graham Moore', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sesam', 'Sesam Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'Sesam', 'Sesam Documentation',
   author, 'Sesam', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
