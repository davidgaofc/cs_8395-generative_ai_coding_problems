class Student:
    """
    A class representing a student and their course enrollment.
    """

    def __init__(self, name, courses=[]):
        """
        Initializes a Student with the provided name and optional list of courses.

        Args:
            name (str): The name of the student.
            courses (list): List of courses the student is enrolled in.
        """
        self.name = name
        self.courses = courses

    def enroll(self, course):
        """
        Enrolls the student in the given course.

        Args:
            course (str): The name of the course to enroll in.
        """
        pass

    def drop(self, course):
        """
        Drops the given course from the student's enrollment.

        Args:
            course (str): The name of the course to drop.
        """
        pass

    def get_courses(self):
        """
        Returns a list of courses the student is currently enrolled in.

        Returns:
            list: List of course names.
        """
        pass