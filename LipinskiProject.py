#!/usr/bin/env python3

#import packages
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Seq import translate
import sys

#supress warning message
import warnings
warnings.simplefilter("ignore", category=Warning)


#read FASTA file
fasta_file = sys.argv[1]
records = list(SeqIO.parse(fasta_file, "fasta"))

#60%: print first 10 sequence IDs
for i in range(10):
    print(records[i].id)

#70%: print the number of sequences without start codons
#start codon function
def has_start_codon(sequence):
    return sequence[:3] == "ATG"

no_start_count = 0
for record in records:
    sequence = str(record.seq)
    #check for start codon
    if not has_start_codon(sequence):
        record.id += ";noStart"
        no_start_count += 1
        
print(f"Sequences without a start codon: {no_start_count}")

    
#80: print the number of sequences without stop codons
#stop codon function
def has_stop_codon(sequence):
    return sequence[-3:] in {"TAA", "TAG", "TGA"}

no_stop_count = 0
for record in records:
    sequence = str(record.seq)
    #check for stop codon
    if not has_stop_codon(sequence):
        record.id += ";noStop"
        no_stop_count += 1

print(f"Sequences without a stop codon: {no_stop_count}")


#90%: print the number of sequences with a length that is not a multiple of three
#multiple of three function
def mult_three(sequence):
    return len(sequence) % 3 == 0

no_mult3_count = 0
for record in records:
    sequence = str(record.seq)
    #check for sequence length that is not a multiple of three
    if not mult_three(sequence):
        record.id += ";noMult3"
        no_mult3_count += 1

print(f"Sequences without a multiple of three: {no_mult3_count}")


#100%: print the number of sequences with premature stop codons
#premature stop codon function
def has_premature_stop(sequence):
    return "*" in translate(sequence[:-3])  #exclude last codon

premature_stop_count = 0

#set to make sure I don't add more than one premature stop tag to sequences with more than one premature stop codon
sequences_with_premature_stop = set()

for record in records:
    sequence = str(record.seq)
    #check for premature stop codons
    #make sure to check that each sequence hasn't already been tagged by putting it in the set
    if has_premature_stop(sequence):
        if record.id not in sequences_with_premature_stop:
            record.id += ";preStop"
            premature_stop_count += 1
            sequences_with_premature_stop.add(record.id)

print(f"Sequences with a premature stop codon: {premature_stop_count}")


