# Import the required packages
from Bio import SeqIO
import os       
     
input_folder = "my_fasta"
output_file = "my_fasta.fasta"
sequences = []
i = 0
for file in os.listdir(input_folder):
    if file.endswith(".fasta"):
        i = i + 1
        filepath = os.path.join(input_folder, file)
        with open(filepath) as f:
            try:
                record = next(SeqIO.parse(f, "fasta"))
                if "NNNNN" not in str(record.seq):
                    sequences.append(record)
            except:
                print(f"Error reading file: {file}")

with open(output_file, "w") as f:
    writer = SeqIO.FastaIO.FastaWriter(f, wrap=0)
    writer.write_file(sequences)
    
print(f"Total sequences: {i}")    
print(f"Merged sequences: {len(sequences)}")
