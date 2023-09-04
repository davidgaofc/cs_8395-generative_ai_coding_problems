from problems.problem_40 import CodeAnalyzer


def test_analyze_code():
    code_analyzer = CodeAnalyzer()
    code = """
    for i in range(10):
        print(i)
    if True:
        print("Hello")
    """
    report = code_analyzer.analyze_code(code)

    assert report.get('for') == 1
    assert report.get('in') == 1
    assert report.get('range') == 1
    assert report.get('print') == 2
    assert report.get('if') == 1
    assert report.get('True') == 1