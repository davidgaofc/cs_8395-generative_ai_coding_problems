from problems.problem_29 import Rectangle, Circle

def test_area():
    rectangle = Rectangle(5, 10)
    assert round(rectangle.area(), 2) == 50.00

    circle = Circle(3)
    assert round(circle.area(), 2) == 28.27