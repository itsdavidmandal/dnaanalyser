import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


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


def create_dna_sequence_visualization(sequence, highlights=None):
    """
    Creates a visualization of a DNA sequence.
    Optionally, highlights specific regions of interest.
    """
    print("Highlights:", highlights)

    fig, ax = plt.subplots()
    ax.set_xlim(0, len(sequence))
    ax.set_ylim(0, 1)
    ax.set_xticks(range(len(sequence)))
    ax.set_xticklabels(list(sequence), fontsize=8)

    # Highlight regions of interest
    if highlights:
        for highlight in highlights:
            if isinstance(highlight, int):
                start = end = highlight
            else:
                start, end = highlight
            ax.axvspan(start, end + 1, facecolor='yellow', alpha=0.3)

    ax.set_title("DNA Sequence Visualization")
    plt.show()


def analyze_sequence():
    sequence = entry_sequence.get()
    pattern = entry_pattern.get()

    # Validate the input
    if not sequence.isalpha() or set(sequence) - {'A', 'T', 'G', 'C'}:
        messagebox.showerror("Error", "Invalid input! Please enter a valid DNA sequence.")
        return

    pattern_matches = find_pattern(sequence, pattern)
    gc_content = calculate_gc_content(sequence)
    motifs = find_motifs(sequence, ["ATG", "TAG"])
    coding_regions = predict_protein_coding_regions(sequence)

    result = "DNA Sequence: {}\n".format(sequence)

    if len(pattern_matches) > 0:
        result += "Pattern '{}' Matches: {}\n".format(pattern, pattern_matches)
    else:
        result += "Pattern '{}' not found in the sequence.\n".format(pattern)

    result += "GC Content: {:.2f}\n".format(gc_content)

    if len(motifs) > 0:
        result += "Motif Matches: {}\n".format(motifs)
    else:
        result += "No motifs found in the sequence.\n"

    if len(coding_regions) > 0:
        result += "Coding Regions: {}\n".format(coding_regions)
    else:
        result += "No protein coding regions found in the sequence.\n"

    # Create DNA sequence visualization
    highlights = pattern_matches + coding_regions
    print("Highlights:", highlights)
    create_dna_sequence_visualization(sequence, highlights)

    # Show the result in a message box
    messagebox.showinfo("Sequence Analysis Result", result)


# Create the main window
window = tk.Tk()
window.title("DNA Sequence Analyzer")

# Create a label and entry field for the sequence input
label_sequence = tk.Label(window, text="Enter a DNA sequence:")
label_sequence.pack(pady=5)

entry_sequence = tk.Entry(window)
entry_sequence.pack()

# Create a label and entry field for the pattern input
label_pattern = tk.Label(window, text="Enter a pattern:")
label_pattern.pack(pady=5)

entry_pattern = tk.Entry(window)
entry_pattern.pack()

# Create a button to trigger the analysis
button = tk.Button(window, text="Analyze", command=analyze_sequence)
button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
