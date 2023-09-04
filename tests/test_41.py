from problems.problem_41 import StringManipulator


def test_capitalize_alternating():
    string_manipulator = StringManipulator()
    input_text = "this is a sample sentence to test the function"
    modified_text = string_manipulator.capitalize_alternating(input_text)

    assert modified_text == "This is A sample Sentence to Test The function"