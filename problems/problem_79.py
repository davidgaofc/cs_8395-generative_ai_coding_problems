class CalendarEvent:
    """
    A class representing a calendar event.
    """

    def __init__(self, event_name, start_time, end_time):
        """
        Initializes a CalendarEvent with event details.

        Args:
            event_name (str): The name of the event.
            start_time (str): The start time of the event in HH:MM format.
            end_time (str): The end time of the event in HH:MM format.
        """
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time

    def duration(self):
        """
        Calculates and returns the duration of the event in minutes.

        Returns:
            int: The duration of the event in minutes.
        """
        pass

    def overlaps(self, other_event):
        """
        Checks if the current event overlaps with another event.

        Args:
            other_event (CalendarEvent): The other event to check.

        Returns:
            bool: True if there is an overlap, False otherwise.
        """
        pass