import os
from robofab.world import OpenFont

#--------------------------------------------
# ufo exported from vfb with vfb2ufo (hints)
#--------------------------------------------

folder = os.pathdirname(__file__)
ufo = os.path.join(folder, "RetiroPro-Regular96pt_vfb2ufo_hints.ufo")
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

print g.lib.keys()
# >> ['com.adobe.type.autohint']

print g.lib['com.adobe.type.autohint']
# >> Data('')
