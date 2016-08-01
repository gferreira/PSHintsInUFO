import os
from robofab.world import OpenFont

#-----------------------------------------------
# ufo exported from vfb with UFOCentral (links)
#-----------------------------------------------

folder = os.path.dirname(__file__)
ufo = os.path.join(folder, "TestFont_UFOCentral_links.ufo")
f = OpenFont(ufo)

#----------------------------
# font-level ps hinting data
#----------------------------

print f.psHints
# >> <PostScript Font Hints Values>

print f.psHints.asDict()
# >> {'vStems': [103, 68, 78, 94, 112, 120], 'blueFuzz': 1, 'otherBlues': [[-290, -285], [-140, -128]], 'blueValues': [[-12, 0], [421, 433], [508, 520], [706, 718]], 'blueShift': 7, 'blueScale': 0.039625, 'hStems': [4, 6]}

#-----------------------------
# glyph-level ps hinting data
#-----------------------------

g = f['B']

print g.psHints
# >> <PostScript Glyph Hints Values>

print g.psHints.hHints
# >> None

print g.psHints.vHints
# >> None

# print g.psHints.hLinks
# >> AttributeError: 'PostScriptGlyphHintValues' object has no attribute 'hLinks'

print g.lib.keys()
# >> ['org.robofab.postScriptHintData']

print g.lib['org.robofab.postScriptHintData']
# >> {'replaceTable': [{'index': 0, 'type': 1}, {'index': 3, 'type': 2}, {'index': 1, 'type': 1}, {'index': 0, 'type': 2}, {'index': 5, 'type': 255}, {'index': 2, 'type': 2}, {'index': 1, 'type': 1}, {'index': 0, 'type': 2}, {'index': 0, 'type': 1}, {'index': 20, 'type': 255}, {'index': 1, 'type': 2}, {'index': 0, 'type': 2}, {'index': 0, 'type': 1}, {'index': 1, 'type': 1}], 'hLinks': [{'node1': 0, 'node2': 11}, {'node1': 8, 'node2': 7}], 'vLinks': [{'node1': 9, 'node2': 18}, {'node1': 20, 'node2': 5}, {'node1': 15, 'node2': 5}, {'node1': 15, 'node2': 2}]}
