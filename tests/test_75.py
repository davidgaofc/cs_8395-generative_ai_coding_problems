from problems.problem_75 import TimeConverter

def test_to_minutes():
    converter = TimeConverter(2, 30)
    result = converter.to_minutes()
    assert result == 150

def test_to_24_hour_format():
    converter = TimeConverter(14, 45)
    result = converter.to_24_hour_format()
    assert result == "14:45"