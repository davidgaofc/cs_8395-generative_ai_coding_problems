from problems.problem_94 import StringManipulator

def test_reverse():
    manipulator = StringManipulator("hello")

    reversed_string = manipulator.reverse()
    assert reversed_string == "olleh"

def test_remove_duplicates():
    manipulator = StringManipulator("hello")

    no_duplicates_string = manipulator.remove_duplicates()
    assert no_duplicates_string == "helo"