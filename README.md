# Python-RNASeq-Annotation

When researching certain strains of yeast for RNA sequencing analysis, an annotation file of the open reading frames does not always exist to be easily downloaded and utilized. Because of this, commonly studied model strains of yeast must be used to transfer genomic coordinates of open reading frames to the experimental strain. During this process, coordinates of sequences in the common strain may not always represent translated open reading frames in the experimental strain because of lack of start/stop codons or presence of premature stop codons. We must check that the new annotation file of the experimental strain only contains sequences that will be transcribed and translated so that the mapping and counting software accurately quantifies the expression of open reading frames. We will do this using the Biopython package and annotation files in FASTA format.

60% Credit  
Load the data from the FASTA file using the SeqIO.parse() function. This will iterate through the sequences and return a SeqRecord object for each sequence with these attributes: sequence, ID, name, description, and dbrefs. To familiarize yourself with manipulating SeqRecord objects, print the first 10 IDs of the sequences.
  
70% Credit  
Check that the sequences begin with a start codon (ATG). For any sequence that does not begin with a start codon, add to the ID a semicolon followed by “noStart” to tag the sequence (ex: id=’NEWG0A04510;noStart’). Print the number of sequences that do NOT begin with a start codon.

80% Credit  
Check that the sequences end with a stop codon (TAA, TAG, or TGA). For any sequence that does not end with a stop codon, add to the ID a semicolon followed by “noStop” to tag the sequence. Print the number of sequences that do NOT end with a stop codon.

90% Credit  
Most yeast genes do not have introns. For the sake of simplicity, we will assume that none of the open reading frames should have introns. Check that the sequence lengths are all multiples of three to ensure proper translation into amino acids. For any sequence that does not have a length that is a multiple of three, add to the ID a semicolon followed by “noMult3” to tag the sequence. Print the number of sequences that do NOT have a length which is a multiple of three.

100% Credit  
Check that the sequences do not have premature stop codons. (Hint: the Bio.Seq package has a translate() function that will translate DNA into amino acids “from Bio.Seq import translate”). Make sure you are not looking for a stop codon at the very end of the sequence. If a sequence has multiple premature stop codons, only count it once in the count of sequences with premature stop codons. For any sequence that has a premature stop codon, add to the ID a semicolon followed by “preStop” to tag the sequence. Print the number of sequences that HAVE premature stop codons.   
(Note: the translate function will give a warning saying that the length of some sequences are not a multiple of three. We obviously know this because we just checked for it in the previous step. The warnings package has a function to ignore warnings: 
import warnings
warnings.simplefilter("ignore", category=Warning)  
Only include this line in your script AFTER you have done every step of the assignment and checked your solutions, as it will suppress all warnings that the script produces.)

