from Bio import SeqIO
import os

# Declare input folder and output folder
input_dir = "./my_sequences"
output_dir= "./my_fasta"

# Check if the folder already exists
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
    print(f"Folder '{output_dir}' created successfully.")
else:
    print(f"Folder '{output_dir}' already exists.")
    
# Loop through each TXT file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        # Construct the full path to the input file
        input_path = os.path.join(input_dir, filename)

        # Read the DNA sequence from the input file
        with open(input_path) as f:
            sequence = f.read().strip()

        # Construct the description for the FASTA file (using the input file name)
        description = filename.replace(".txt", "")

        # Construct the output path for the FASTA file
        output_path = os.path.join(output_dir, filename.replace(".txt", ".fasta"))

        # Write the DNA sequence to the output FASTA file
        with open(output_path, "w") as f:
            f.write(">{}\n{}\n".format(description, sequence))
        
        print(f"Created file: {description}")
    