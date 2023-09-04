from problems.problem_12 import Student, School

def test_add_grade():
    student = Student(1, "Alice")
    student.add_grade("Math", 90.0)
    student.add_grade("Science", 85.0)
    assert "Math" in student.grades
    assert "Science" in student.grades
    assert student.grades["Math"] == 90.0
    assert student.grades["Science"] == 85.0

def test_get_average_grade():
    student = Student(1, "Alice")
    student.add_grade("Math", 90.0)
    student.add_grade("Science", 85.0)
    average_grade = student.get_average_grade()
    assert average_grade == (90.0 + 85.0) / 2

def test_add_student():
    school = School()
    student = Student(1, "Alice")
    school.add_student(student)
    assert student.student_id in school.students
    assert school.students[student.student_id] == student

def test_get_highest_average():
    school = School()

    student1 = Student(1, "Alice")
    student1.add_grade("Math", 90.0)
    student1.add_grade("Science", 85.0)

    student2 = Student(2, "Bob")
    student2.add_grade("Math", 95.0)
    student2.add_grade("Science", 88.0)

    school.add_student(student1)
    school.add_student(student2)

    highest_avg_student = school.get_highest_average()
    assert highest_avg_student.name == "Bob"