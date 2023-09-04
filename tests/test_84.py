from problems.problem_84 import StudentGrades

def test_add_grade():
    grades = StudentGrades()
    grades.add_grade("Alice", 85)
    grades.add_grade("Bob", 92)

    assert "Alice" in grades.grades
    assert "Bob" in grades.grades

def test_get_average_grade():
    grades = StudentGrades()
    grades.add_grade("Alice", 85)
    grades.add_grade("Alice", 90)
    grades.add_grade("Bob", 92)

    assert grades.get_average_grade("Alice") == 87.5
    assert grades.get_average_grade("Bob") == 92

def test_get_highest_grade():
    grades = StudentGrades()
    grades.add_grade("Alice", 85)
    grades.add_grade("Alice", 90)
    grades.add_grade("Bob", 92)

    assert grades.get_highest_grade("Alice") == 90
    assert grades.get_highest_grade("Bob") == 92

def test_get_lowest_grade():
    grades = StudentGrades()
    grades.add_grade("Alice", 85)
    grades.add_grade("Alice", 90)
    grades.add_grade("Bob", 92)

    assert grades.get_lowest_grade("Alice") == 85
    assert grades.get_lowest_grade("Bob") == 92