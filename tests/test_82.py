from problems.problem_82 import Student

def test_enroll():
    student = Student("Alice")
    student.enroll("Math")
    student.enroll("Science")
    assert student.get_courses() == ["Math", "Science"]

def test_drop():
    student = Student("Bob", ["English", "History"])
    student.drop("History")
    assert student.get_courses() == ["English"]

def test_get_courses():
    student = Student("Alice")
    student.enroll("Math")
    student.enroll("Science")
    assert student.get_courses() == ["Math", "Science"]
    student = Student("Bob", ["English", "History"])
    student.drop("History")
    assert student.get_courses() == ["English"]

