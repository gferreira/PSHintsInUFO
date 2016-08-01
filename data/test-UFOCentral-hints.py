import os
from robofab.world import OpenFont

#-----------------------------------------------
# ufo exported from vfb with UFOCentral (hints)
#-----------------------------------------------

folder = os.path.dirname(__file__)
ufo = os.path.join(folder, "TestFont_UFOCentral_hints.ufo")
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
# >> [[0, 4], [702, 4]]

print g.psHints.vHints
# >> [[97, 120], [425, 122], [439, 108], [439, 136]]

print g.lib.keys()
# >> ['org.robofab.postScriptHintData']

print g.lib['org.robofab.postScriptHintData']
# >> {'replaceTable': [{'index': 0, 'type': 1}, {'index': 3, 'type': 2}, {'index': 1, 'type': 1}, {'index': 0, 'type': 2}, {'index': 5, 'type': 255}, {'index': 2, 'type': 2}, {'index': 1, 'type': 1}, {'index': 0, 'type': 2}, {'index': 0, 'type': 1}, {'index': 20, 'type': 255}, {'index': 1, 'type': 2}, {'index': 0, 'type': 2}, {'index': 0, 'type': 1}, {'index': 1, 'type': 1}], 'vHints': [[97, 120], [425, 122], [439, 108], [439, 136]], 'hHints': [[0, 4], [702, 4]]}
