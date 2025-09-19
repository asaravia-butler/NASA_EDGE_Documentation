# Configuration file for the Sphinx documentation builder.

project = 'NASA EDGE Documentation'
copyright = '2025, GeneLab and LANL'
author = 'GeneLab and LANL'
version = 'latest'

# Inject project name into rst files if needed
rst_epilog = f"""
.. |project_name| replace:: {project}
"""

# Add extensions
extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx', # To do: implement
    'sphinx_copybutton',
    'sphinx_design',
    'hoverxref.extension',
]

autosectionlabel_prefix_document = True 

# Myst extension's extensions
myst_enable_extensions = [
    "dollarmath",  # Enables $ signs for math
    "amsmath",     # Supports more complex math via LaTeX
    "deflist",     # Definition lists
    "html_admonition",  # TO do: implement
    "html_image",  # Render plain html img tags in docs  
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Custom Styling
html_title = project
html_logo = "_static/images/NASA_EDGE_logos.png"
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style_nav_header_background': "#105bd8",
    'sticky_navigation': True,
    'collapse_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_show_sphinx = False
html_show_copyright = False

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

html_context = {
    "display_github": True,
    "github_user": "asaravia-butler",
    "github_repo": "NASA_EDGE_Documentation",
    "github_version": "main",
    "conf_py_path": "/source/"
}

# Hoverxref configuration
hoverxref_auto_ref = True  # Auto-enable on all :ref: roles
hoverxref_api_host = 'https://readthedocs.org'
hoverxref_roles = ['term', 'ref']  # Enable hover tooltips on glossary terms and refs
hoverxref_role_types = {
    'term': 'tooltip',  # Use tooltip style for glossary terms
    'ref': 'tooltip',   # Use tooltip style for ref links
}
