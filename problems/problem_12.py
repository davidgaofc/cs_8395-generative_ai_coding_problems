class Student:
    def __init__(self, student_id, name):
        """
        Represents a student in a record system.

        Args:
            student_id (int): Unique student identifier.
            name (str): Student's name.
        """
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        """
        Adds a grade for a specific course.

        Args:
            course (str): Course name.
            grade (float): Grade obtained in the course.
        """
        # TODO: Implement this function to add a grade for the student.
        pass

    def get_average_grade(self):
        """
        Calculates the average grade of the student.

        Returns:
            float: Average grade.
        """
        # TODO: Implement this function to calculate and return the average grade.
        pass

class School:
    def __init__(self):
        """
        Represents a school record system.

        This class allows administrators to manage student records, add students,
        and calculate statistics for the entire school.
        """
        self.students = {}

    def add_student(self, student):
        """
        Adds a student to the school record system.

        Args:
            student (Student): Student object to be added.
        """
        # TODO: Implement this function to add a student to the school.
        pass

    def get_highest_average(self):
        """
        Retrieves the student with the highest average grade in the school.

        Returns:
            Student: Student with the highest average grade.
        """
        # TODO: Implement this function to find and return the student with the highest average grade.
        pass