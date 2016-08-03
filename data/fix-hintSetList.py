import os
from random import randint

def fix_hintsetlist(ufo_path):

    glyphs_folder = os.path.join(ufo_path, 'glyphs')
    glifs = [g for g in os.listdir(glyphs_folder) if os.path.splitext(g)[-1] == '.glif']

    for g in glifs:
        glif_path = os.path.join(glyphs_folder, g)
        glif_data = open(glif_path, 'r').read()

        # if the glif data has a `hintSetList` element
        if glif_data.find('hintSetList') != -1:
            # generate a random number
            id_attr = ''.join([str(randint(0, 9)) for n in range(20)])
            # insert `id` attribute with dummy value
            glif_new = glif_data.replace('<hintSetList>', '<hintSetList id="%s">' % id_attr)
            # delete the original .glif file
            os.remove(glif_path)
            # write the modified .glif data in its place
            f = open(glif_path, 'w')
            f.write(glif_new)
            f.close()

if __name__ == '__main__':

    folder = os.path.dirname(__file__)
    ufo_path = os.path.join(folder, "TestFont1_vfb2ufo_hints.ufo")

    fix_hintsetlist(ufo_path)
