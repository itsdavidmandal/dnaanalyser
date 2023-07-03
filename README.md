# dnaanalyser
The provided code is a collection of functions for performing various DNA sequence analyses. It offers several functionalities to analyze DNA sequences, including finding patterns, calculating GC content, identifying motifs, and predicting protein coding regions.



# DNA Sequence Analysis

This code provides several functions for analyzing DNA sequences, including finding patterns, calculating GC content, identifying motifs, and predicting protein coding regions.

## Functions

1. `find_pattern(sequence, pattern)`: Finds occurrences of a pattern in a DNA sequence and returns a list of starting indices of the pattern matches.

2. `calculate_gc_content(sequence)`: Calculates the GC content of a DNA sequence and returns the GC content as a percentage.

3. `find_motifs(sequence, motifs)`: Finds motifs (subsequences) in a DNA sequence and returns a list of starting indices of the motif matches.

4. `predict_protein_coding_regions(sequence)`: Predicts protein coding regions in a DNA sequence and returns a list of protein coding regions as tuples of start and end indices.

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

