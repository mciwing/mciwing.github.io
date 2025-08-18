---
date:
  created: 2025-08-18
readtime: 2
pin: true
authors:
    - armin_muzaferovic
slug: landslides
tags:
  - Master Thesis
  - Landslides
  - GUI
---

# Master Thesis - Landslide Pipeline

TLDR: Landslide Pipeline is a tool that lets you select a place and time and
run a trained Machine Learning model to identify landslides using satellite
images. It is designed to also be accessible for non-developers.
:satellite: :world_map:

<p align="center">
  <a href="https://github.com/muzaferovarmin/LandslideMA" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Landslide-181717?logo=github&style=for-the-badge" alt="GitHub">
  </a>
</p>

<!-- more -->

---

???+ info

    This project was completed as a Master's thesis supervised by Jakob Klotz.
    The post was written by the student, Armin Muzaferovic.


## What is Landslide Pipeline?

In short, the repo contains all the necessary code to select a time and place
using a GUI to then be able to detect landslides with the selected parameters.
The model in the background was trained using the
[landslide4sense](https://github.com/iarai/Landslide4Sense-2022) baseline
model and the provided dataset. GUI was done using
[CustomTKinter](https://github.com/TomSchimansky/CustomTkinter) as well as
[TkinterMap](https://github.com/TomSchimansky/TkinterMapView).

## How does it work?

When selecting the area on the provided map in the GUI, a request is sent to
the ESA Copernicus API with the corresponding parameters. In the query to the
API, 12 Layers of the Sentinel2-L1C Satellite and the Copernicus30 DEM Data are
requested. After receiving the data and calculating the slope from the digital 
elevation model, the data is formatted for use with the machine learning model.
After user confirmation, the data for each pixel is evaluated to check if there
is a landslide detected or not.

## Why Landslide Pipeline?

While there are already great models for landslide detection, the next step is
to make it easier to generate training data or to check whether a specific 
region has experienced a landslide. The goal of this implementation was to 
simplify future research in the field of machine learning with satellite data, 
making it easier to use available datasets. For example, city administrations 
could use this tool to check their areas for possible landslide risks.

## How to use it?

Simply visit [GitHub - muzaferovarmin/LandslideMA](https://github.com/muzaferovarmin/LandslideMA)
and either download the precompiled executable file for your OS or clone the
repo and build the Python :fontawesome-brands-python: code yourself! After
that, use your free Copernicus Dataspace account (which can be created
[here](https://browser.dataspace.copernicus.eu/)) to generate your API
credentials to use and you are ready to go!
