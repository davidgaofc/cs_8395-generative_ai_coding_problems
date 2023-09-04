from problems.problem_64 import Rectangle

def test_area():
    rectangle = Rectangle(5, 10)
    assert rectangle.area() == 50



def test_perimeter():
    rectangle = Rectangle(5, 10)
    assert rectangle.perimeter() == 30

