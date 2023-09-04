from problems.problem_59 import RomanNumeralConverter

def test_to_integer():
    converter = RomanNumeralConverter()
    assert converter.to_integer("III") == 3
    assert converter.to_integer("IX") == 9
    assert converter.to_integer("LVIII") == 58

def test_to_roman():
    converter = RomanNumeralConverter()
    assert converter.to_roman(4) == "IV"
    assert converter.to_roman(58) == "LVIII"
    assert converter.to_roman(1994) == "MCMXCIV"