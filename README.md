# dnaanalyser
The provided code is a collection of functions for performing various DNA sequence analyses. It offers several functionalities to analyze DNA sequences, including finding patterns, calculating GC content, identifying motifs, and predicting protein coding regions.



# DNA Sequence Analysis

This code provides several functions for analyzing DNA sequences, including finding patterns, calculating GC content, identifying motifs, and predicting protein coding regions.

## Functions

1. `find_pattern(sequence, pattern)`: Finds occurrences of a pattern in a DNA sequence and returns a list of starting indices of the pattern matches.

2. `calculate_gc_content(sequence)`: Calculates the GC content of a DNA sequence and returns the GC content as a percentage.

3. `find_motifs(sequence, motifs)`: Finds motifs (subsequences) in a DNA sequence and returns a list of starting indices of the motif matches.

4. `predict_protein_coding_regions(sequence)`: Predicts protein coding regions in a DNA sequence and returns a list of protein coding regions as tuples of start and end indices.
Breakdown of the output 
5. DNA Sequence: ATGGTACCCTAAATGTAGCTAGCTAAAGTCCCATG Pattern Matches: [9, 23] GC Content: 42.857142857142854 Motif Matches: [8, 12, 32, 15, 19] Coding Regions: [(0, 11), (12, 17)]

Process finished with exit code 0

The provided DNA sequence is "ATGGTACCCTAAATGTAGCTAGCTAAAGTCCCATG". Let's break down the results obtained from the code:

1. Pattern Matches: The pattern "TAA" was searched within the DNA sequence, and it was found at indices 9 and 23.

2. GC Content: The GC content of the DNA sequence was calculated to be approximately 42.86%. This value represents the percentage of nucleotides in the sequence that are either Guanine (G) or Cytosine (C).

3. Motif Matches: The motifs "ATG" and "TAG" were searched within the DNA sequence. The motif "ATG" was found at indices 8 and 12, while the motif "TAG" was found at indices 32 and 15. The motif "TAG" was also found at index 19.

4. Coding Regions: The code predicted the protein coding regions in the DNA sequence. It identified two coding regions: one from index 0 to 11 and another from index 12 to 17. These regions are potential locations where protein-coding genes may be present.

The process finished with exit code 0, indicating that the code executed successfully without any errors or issues.

## Example Usage

```python
dna_sequence = "ATGGTACCCTAAATGTAGCTAGCTAAAGTCCCATG"
pattern = "TAA"
motifs = ["ATG", "TAG"]
coding_regions = predict_protein_coding_regions(dna_sequence)

print("DNA Sequence:", dna_sequence)
print("Pattern Matches:", find_pattern(dna_sequence, pattern))
print("GC Content:", calculate_gc_content(dna_sequence))
print("Motif Matches:", find_motifs(dna_sequence, motifs))
print("Coding Regions:", coding_regions)

