from problems.problem_93 import DNAAnalyzer

def test_gc_content():
    analyzer = DNAAnalyzer("ATCGATTAGCG")
    assert analyzer.gc_content() == 50.0
def test_count_nucleotides():
    analyzer = DNAAnalyzer("ATCGATTAGCG")
    assert analyzer.count_nucleotides() == {'A': 3, 'T': 4, 'C': 2, 'G': 3}
def test_reverse_complement():
    analyzer = DNAAnalyzer("ATCGATTAGCG")
    assert analyzer.reverse_complement() == "CGCTAATCGAT"
