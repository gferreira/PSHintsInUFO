PS Hints in UFO
===============

This repository contains information, scripts and data to assist in the process of defining a standard format for storing PS hints in UFO.

why?
----

- PS hints are not covered by the [UFO specification](http://unifiedfontobject.org/)
- PS hints are important for low-resolution printers and on-screen display
- PS hints often need to be edited manually (autohint on font generation is not good enough)
- there are different, non-standard implementations of PS hints in UFO (RoboFab/Superpolator, AFDKO/vfb2ufo)
- manual hints are currently not supported in a RoboFont-based workflow
