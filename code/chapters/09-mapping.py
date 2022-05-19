# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Making maps with Python {#map-making}
#
# ## Introduction
#
# - Geopandas explore has been used in previous chapters.
# - When to focus on visualisation? At the end of geographic data processing workflows.
#
# <!-- Input datasets: https://github.com/geocompr/spDatapy -->
# <!-- Decision of whether to use static or interactive. -->
# <!-- Flow diagram? -->

import matplotlib as mpl
import geopandas as gpd
nz = gpd.read_file("data/nz.gpkg") 

# ## Static maps
#
# - Focus on matlibplot
# - First example: NZ with fill and borders
# - Scary matplotlib code here...

nz.plot(color="grey")
nz.plot(color="none", edgecolor="blue")

# <!-- # Add fill layer to nz shape
# tm_shape(nz) +
#   tm_fill() 
# # Add border layer to nz shape
# tm_shape(nz) +
#   tm_borders() 
# # Add fill and border layers to nz shape
# tm_shape(nz) +
#   tm_fill() +
#   tm_borders()  -->
#
# ### Palettes
# ### Layers
# ### Faceted maps
# ### Exporting maps as images
#
# <!-- ## Animated maps -->
# ## Interactive maps
#
# - When are interactive maps useful
# - Holoviews: facetted plotting
# - Panel: allows you to create applications/dashboards
#
# ### GeoPandas explore
# ### Layers
# ### Publishing interactive maps
# ### Linking geographic and non-geographic visualisations
#
# <!-- ## Mapping applications Streamlit? -->
#
# ## Exercises
