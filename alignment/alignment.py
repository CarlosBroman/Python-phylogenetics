import Bio.Align.Applications
dir(Bio.Align.Applications)

from Bio.Align.Applications import ClustalwCommandline
cline = ClustalwCommandline("clustalw2", infile="sharks.fasta")
print(cline)