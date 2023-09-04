class DNAAnalyzer:
    """
    A class for analyzing DNA sequences.
    """

    def __init__(self, dna_sequence):
        """
        Initializes the DNAAnalyzer object with a DNA sequence.

        Args:
            dna_sequence (str): The input DNA sequence.
        """
        self.dna_sequence = dna_sequence

    def gc_content(self):
        """
        Calculates the GC content of the DNA sequence.

        Returns:
            float: The GC content as a percentage.
        """
        pass

    def count_nucleotides(self):
        """
        Counts the occurrences of each nucleotide in the DNA sequence.

        Returns:
            dict: A dictionary with nucleotide counts.
        """
        pass

    def reverse_complement(self):
        """
        Generates the reverse complement of the DNA sequence.

        Returns:
            str: The reverse complement DNA sequence.
        """
        pass