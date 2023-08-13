from ete3 import Tree, faces, TreeStyle, PhyloTree
from Bio import AlignIO

t = PhyloTree("sharks.dnd")
print(t)

img_path = "./"

max_image_width = 250
max_image_height = 150

greatwhiteFace = faces.ImgFace(img_path+"GreatWhite.png", width=max_image_width, height=max_image_height)
tigersharkFace = faces.ImgFace(img_path+"TigerShark.png", width=max_image_width, height=max_image_height)

nameFace = faces.AttrFace("name", fsize=20, fgcolor="#009000")

code2name = {
    "L08031.1":"Great White Shark",
    "L08034.1":"Galeocerdo cuvier",
    "JF950299.1":"Ginglymostoma cirratum",
    "L08035.1":"Heterodontus fransci",
    "L08036.1":"Isurus oxyrhynchus",
    "EU528661.1":"Mitsukurina owstoni",
    "L08040.1":"Prionace glauca"
}

code2desc = {
    "L08031.1": """The Great White Shark (Carcharodon carcharias) is the biggest shark in the ocean nowadays.""",
    "L08034.1":"""The Tiger Shark (Galeocerdo cuvier) desc""",
    "JF950299.1":"""Ginglymostoma cirratum desc""",
    "L08035.1":"""Heterodontus fransci desc""",
    "L08036.1":"""Isurus oxyrhynchus desc""",
    "EU528661.1":"""Mitsukurina owstoni desc""",
    "L08040.1":"""Prionace glauca desc"""
}

def mylayout(node):
    if node.is_leaf():
        # Add an static face that handles the node name
        faces.add_face_to_node(nameFace, node, column=0)
        # We can also create faces on the fly
        longNameFace = faces.TextFace(code2name[node.name])
        faces.add_face_to_node(longNameFace, node, column=0)

        # text faces support multiline. We add a text face
        # with the whole description of each leaf.
        descFace = faces.TextFace(code2desc[node.name], fsize=10)
        descFace.margin_top = 10
        descFace.margin_bottom = 10
        descFace.border.margin = 1

        # Note that this faces is added in "aligned" mode
        faces.add_face_to_node(descFace, node, column=0, aligned=True)

        # Sets the style of leaf nodes
        node.img_style["size"] = 12
        node.img_style["shape"] = "circle"
    #If node is an internal node
    else:
        # Sets the style of internal nodes
        node.img_style["size"] = 6
        node.img_style["shape"] = "circle"
        node.img_style["fgcolor"] = "#000000"
    
    
    if len(node)<=1:  
        col = 0
    
        for i, name in enumerate(set(node.get_leaf_names())):
            if i>0 and i%2 == 0:
                col += 1
            if name.startswith("L08031.1"):
                faces.add_face_to_node(greatwhiteFace, node, column = col)
            elif name.startswith("L08034.1"):
                faces.add_face_to_node(tigersharkFace, node, column = col)
            elif name.startswith("JF950299.1"):
                faces.add_face_to_node(greatwhiteFace, node, column = col)
            elif name.startswith("L08035.1"):
                faces.add_face_to_node(greatwhiteFace, node, column = col)
            elif name.startswith("L08036.1"):
                faces.add_face_to_node(greatwhiteFace, node, column = col)
            elif name.startswith("EU528661.1"):
                faces.add_face_to_node(greatwhiteFace, node, column = col)
            elif name.startswith("L08040.1"):
                faces.add_face_to_node(greatwhiteFace, node, column = col)
                
            # Modifies this node's style
            node.img_style["size"] = 16
            node.img_style["shape"] = "sphere"
            node.img_style["fgcolor"] = "#AA0000"



alignment = AlignIO.read("sharks.aln", "clustal")
AlignIO.write(alignment, "sharks.fasta", "fasta")

ts = TreeStyle()
ts.layout_fn = mylayout
t.link_to_alignment(alignment="sharks.fasta", alg_format="fasta")
t.render("mytree.png", w=600, units="mm", tree_style = ts)
t.show()
