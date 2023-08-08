import time
import csv
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO

# Read the input fasta file
fasta_file = "my_fasta.fasta"
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')

# Record start time
start_time = time.time()

with open("blast_results.csv", "a", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Query description", "Hit id", "Hit description", "Hit accession", "Query coverage", "Percentage identity", "Query", "Identities", "Positives", "Gaps", "Strand", "Alignment length", "Query start", "Query end"])
# Iterate over the fasta sequences
    for fasta in fasta_sequences:
        # Print the description of the current fasta sequence
        print("Query description:", fasta.description)

        # Perform BLAST search and print progress message
        print("Running BLAST search...")
        max_hits = 10
        result_handle = NCBIWWW.qblast("blastn", "nt", str(fasta.seq), hitlist_size=max_hits)
        print("BLAST search complete!")

        # Parse BLAST result and print progress message
        print("Parsing BLAST results...")
        blast_record = NCBIXML.read(result_handle)
        print("BLAST results parsed!")

        # Print out the top hit information and progress message
        print("Processing top hit...")
        alignment = blast_record.alignments[0]
        hit_id = alignment.hit_id
        hit_def = alignment.hit_def
        accession = alignment.accession
        print("Processing top hit complete!")

        print("Processing HSPs...")


        for hsp in alignment.hsps:
            query_coverage = hsp.align_length / len(fasta)
            perc_identity = hsp.identities / hsp.align_length
            csv_writer.writerow([fasta.description, hit_id, hit_def, accession, query_coverage, perc_identity, hsp.query, hsp.identities, hsp.positives, hsp.gaps, hsp.strand, hsp.align_length, hsp.query_start, hsp.query_end])
        print("Processing HSPs complete!")

# Record end time and calculate time taken
end_time = time.time()
time_taken = end_time - start_time
print("Time taken: {:.2f} seconds".format(time_taken))