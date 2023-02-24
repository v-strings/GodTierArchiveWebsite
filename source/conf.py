# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LTG'
copyright = '2023, strings'
author = 'strings'
epub_contributor = "Stainbine, izzastor"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_design','sphinxcontrib.video','sphinxext.opengraph']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
source_encoding = 'utf-8-sig'

ogp_site_name = "GodTierArchive"
ogp_site_url = "https://godtierarchivewebsite.readthedocs.io"
ogp_image = "https://cdn.discordapp.com/attachments/836639325961322546/1077627814662123632/magik.jpg"
