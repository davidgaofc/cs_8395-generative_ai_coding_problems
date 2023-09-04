from problems.problem_53 import DNAAnalyzer

def test_calculate_gc_content():
    sequence = "ATCGATCGCGTAAGCTAGCTAGCTA"
    analyzer = DNAAnalyzer(sequence)
    gc_content = analyzer.calculate_gc_content()

    assert gc_content == 45.83