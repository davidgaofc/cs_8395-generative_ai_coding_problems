from problems.problem_68 import TemperatureConverter

def test_celsius_to_fahrenheit():
    converter = TemperatureConverter()
    assert converter.celsius_to_fahrenheit(0) == 32.0
    assert converter.celsius_to_fahrenheit(100) == 212.0
    assert converter.celsius_to_fahrenheit(-40) == -40.0


def test_fahrenheit_to_celsius():
    converter = TemperatureConverter()
    assert converter.fahrenheit_to_celsius(32) == 0.0
    assert converter.fahrenheit_to_celsius(212) == 100.0
    assert converter.fahrenheit_to_celsius(-40) == -40.0