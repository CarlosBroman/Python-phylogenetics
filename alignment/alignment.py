import Bio.Align.Applications
dir(Bio.Align.Applications)

import os
from Bio.Align.Applications import ClustalwCommandline
clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile="sharks.fasta")

assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()
