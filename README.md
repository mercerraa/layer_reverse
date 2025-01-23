---
title: Layer Reverse
author:
- name: Andrew Mercer
  affiliation: Riksantikvarieämbetet
  email: andrew.mercer@raa.se
date:  2025.01.23
lang: en-GB
papersize: a4
geometry:
- margin=2cm
- portrait
font: 11
mainfont: "Georgia"
indent: false
linestretch: 1.2
---

# Description

The Layer Reverse QGIS plugin has only one function: to reverse the order of layers as shown in the Contents panel.
Highlight the layers to be reversed and then click on the button in the Plugin toolbar.

The plugin reverses the order of those plugins highlighted in the Contents, it will leave all other layers untouched.

# Why

The plugin came about mostly because of a wms from Lantmäteriet (Sweden) that loads a topographic map in seperate layers but in reverse order.
The text layer ends up at the bottom and the polygon layer with landuse is put on top.

The problem is not unique to this particular case and arises when importing other large datasets.