from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
# from Bio.Phylo.Consensus import bootstrap_consensus, majority_consensus

align = AlignIO.read("sharks.aln", "clustal")
print(align)

tree = Phylo.read("sharks.dnd", "newick")
Phylo.draw_ascii(tree)


calculator = DistanceCalculator('identity')
dm = calculator.get_distance(align)
print(dm)

constructor = DistanceTreeConstructor()

upgmatree = constructor.upgma(dm)
print(upgmatree)
Phylo.draw_ascii(upgmatree)

njtree = constructor.nj(dm)
print(njtree)
Phylo.draw_ascii(njtree)


# consensus_tree = bootstrap_consensus(align, 10, constructor, majority_consensus)