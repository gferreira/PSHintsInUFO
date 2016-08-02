PS Hints in UFO
===============

This repository contains information, scripts and data to assist in the process of defining a standard format for storing PS hints in UFO.


0. Introduction
---------------

- PS hints are not (yet) covered by the [UFO specification](http://unifiedfontobject.org/)
- PS hints are important for low-resolution printers and on-screen display
- PS hints often need to be edited manually (autohint on font generation is not good enough)
- there are different, non-standard implementations of PS hints in UFO (RoboFab/Superpolator, AFDKO/vfb2ufo)
- manual hints are currently not supported in a RoboFont-based workflow


1. Available formats and implementations
----------------------------------------

### 1.1. RoboFab / UFOCentral

- [font-level][1] and [glyph-level][2] `psHints` attributes: `f.psHints`, `g.psHints`
- API documented in the RoboFab documentation
- supports both hints and FL “links”
- glyph hints can be acessed and manipulated with Python
- Superpolator3 can interpolate between links (but not between hints)
- font-level data is also available in the `RInfo` object
- glyph-level data is also available in `g.lib['org.robofab.postScriptHintData']`
- font- and glyph-level `psHints` attributes are not available in RoboFont’s wrapper objects

[1]: http://robodocs.info/roboFabDocs/source/objects/psHints.html
[2]: http://robodocs.info/roboFabDocs/source/objects/psHintsGlyph.html

#### Test scripts and sample files

- [test-UFOCentral-hints.py](data/test-UFOCentral-hints.py)
- [example `.glif` file with hints](data/TestFont_UFOCentral_hints.ufo/glyphs/B_.glif)
- [test-UFOCentral-links.py](data/test-UFOCentral-links.py)
- [example `.glif` file with links](data/TestFont_UFOCentral_links.ufo/glyphs/B_.glif')

### 1.2. AFDKO autohint

- AFDKO’s `autohint` can be applied to UFOs
- by default, hints are stored in a separate UFO3 layer named `glyphs.com.adobe.type.processedGlyphs`
- hints can also be stored in the default layer (with the argument `-wd`)
- glyph-level data is stored in `g.lib['com.adobe.type.autohint']`
- glyph hints are wrapped in a `<data>` tag and cannot be acessed or manipulated with RoboFab

#### Tests and examples

- [example `.glif` file with hints (autohinted with AFDKO)](data/TestFont_AFDKO-autohint.ufo/glyphs.com.adobe.type.processedGlyphs/B_.glif)

### 1.3. vfb2ufo

- follows the AFDKO format, with hints stored in the default layer
- produces the same output for hints and links

#### Problems

In current tests, an error is raised when trying to generate `.otf` from an UFO converted with vfb2ufo:

    parseT1HintData: unhandled token: <hintSetList>
    tx: (ufr) Encountered <hintset> when not under <hintSetList>. Glyph: B. Context: etList>
        <hintset pointTag="hr00">
          <hstem pos="0" width
    .
    tx: fatal error

#### Tests and examples

- [test-vfb2ufo-hints-links.py](data/test-vfb2ufo-hints-links.py)
- [example `.glif` file with hints](data/TestFont_vfb2ufo_hints.ufo/glyphs/B_.glif) / [links](data/TestFont_vfb2ufo_links.ufo/glyphs/B_.glif) (same output)


2. Comments
-----------

- there should be one standard way to describe hints in UFOs!
- PS hints should be covered by the UFO specification
- all implementations of PS hints in UFO (AFDKO, RoboFont, FontLab & others) should follow the specified format
- it should be possible to manually edit PS hints in RoboFont (extension?)
