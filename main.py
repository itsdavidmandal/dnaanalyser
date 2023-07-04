import tkinter as tk
from tkinter import messagebox


def find_pattern(sequence, pattern):
    """
    Finds occurrences of a pattern in a DNA sequence.
    Returns a list of starting indices of the pattern matches.
    """
    matches = []
    pattern_length = len(pattern)
    sequence_length = len(sequence)

    for i in range(sequence_length - pattern_length + 1):
        if sequence[i:i + pattern_length] == pattern:
            matches.append(i)

    return matches



def calculate_gc_content(sequence):
    """
    Calculates the GC content of a DNA sequence.
    Returns the GC content as a percentage.
    """
    gc_count = 0
    total_count = 0

    for nucleotide in sequence:
        if nucleotide == 'G' or nucleotide == 'C':
            gc_count += 1
        total_count += 1

    gc_content = (gc_count / total_count) * 100
    return gc_content




def find_motifs(sequence, motifs):
    """
    Finds motifs (subsequences) in a DNA sequence.
    Returns a list of starting indices of the motif matches.
    """
    matches = []

    for motif in motifs:
        pattern_length = len(motif)
        sequence_length = len(sequence)

        for i in range(sequence_length - pattern_length + 1):
            if sequence[i:i + pattern_length] == motif:
                matches.append(i)

    return matches




def predict_protein_coding_regions(sequence):
    """
    Predicts protein coding regions in a DNA sequence.
    Returns a list of protein coding regions as tuples of start and end indices.
    """
    regions = []
    in_coding_region = False
    sequence_length = len(sequence)

    for i in range(sequence_length - 2):
        codon = sequence[i:i + 3]

        if codon == 'ATG' and not in_coding_region:
            start_index = i
            in_coding_region = True
        elif (codon == 'TAA' or codon == 'TAG' or codon == 'TGA') and in_coding_region:
            end_index = i + 2
            regions.append((start_index, end_index))
            in_coding_region = False

    return regions


def analyze_sequence():
    sequence = entry.get()

    pattern = "TAA"
    motifs = ["ATG", "TAG"]
    coding_regions = predict_protein_coding_regions(sequence)

    result = ""
    result += "DNA Sequence: {}\n".format(sequence)
    result += "Pattern Matches: {}\n".format(find_pattern(sequence, pattern))
    result += "GC Content: {:.2f}\n".format(calculate_gc_content(sequence))
    result += "Motif Matches: {}\n".format(find_motifs(sequence, motifs))
    result += "Coding Regions: {}\n".format(coding_regions)

    # Show the result in a message box
    messagebox.showinfo("Sequence Analysis Result", result)


# Create the main window
window = tk.Tk()
window.title("DNA Sequence Analyzer")

# Create a label for instructions
label = tk.Label(window, text="Enter a DNA sequence:")
label.pack(pady=10)

# Create an entry field for user input
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger the analysis
button = tk.Button(window, text="Analyze", command=analyze_sequence)
button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
