#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class Shape:
    def __init__(self):
        """
        Represents a base class for geometric shapes.

        This class allows users to create and compute areas of geometric shapes.
        """

    # TODO: Implement this function
    def area(self):
        """
        Computes the area of the shape.

        Returns:
            float: The computed area.
        """
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Represents a rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    # TODO: Implement this function
    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            float: The computed area of the rectangle.
        """
        pass


class Circle(Shape):
    def __init__(self, radius):
        """
        Represents a circle.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    # TODO: Implement this function
    def area(self):
        """
        Computes the area of the circle.

        Returns:
            float: The computed area of the circle.
        """
        pass