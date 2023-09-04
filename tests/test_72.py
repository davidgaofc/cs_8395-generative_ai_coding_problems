from problems.problem_72 import ColorPalette

def test_add_color():
    palette = ColorPalette()
    palette.add_color("red")
    palette.add_color("green")
    palette.add_color("blue")
    assert palette.get_colors() == ["red", "green", "blue"]

def test_remove_color():
    palette = ColorPalette()
    palette.add_color("red")
    palette.add_color("green")
    palette.add_color("blue")

    assert palette.remove_color("green") is True
    assert palette.remove_color("yellow") is False

    assert palette.get_colors() == ["red", "blue"]

def test_get_colors():
    palette = ColorPalette()
    palette.add_color("orange")
    palette.add_color("purple")
    palette.add_color("pink")
    assert palette.get_colors() == ["orange", "purple", "pink"]