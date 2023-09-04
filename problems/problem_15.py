class Task:
    def __init__(self, name, description, priority):
        """
        Represents a task in the task management system.

        Args:
            name (str): Name of the task.
            description (str): Description of the task.
            priority (int): Priority of the task (higher value indicates higher priority).
        """
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = False

    # TODO: Implement this function
    def complete(self):
        """
        Marks the task as completed.
        """
        pass

class TaskList:
    def __init__(self, name):
        """
        Represents a list of tasks in the task management system.

        Args:
            name (str): Name of the task list.
        """
        self.name = name
        self.tasks = []

    # TODO: Implement this function
    def add_task(self, task):
        """
        Adds a task to the task list.

        Args:
            task (Task): Task object to be added.
        """
        pass

    # TODO: Implement this function
    def get_high_priority_tasks(self):
        """
        Retrieves a list of high-priority tasks in the task list.

        Returns:
            list: List of high-priority Task objects.
        """
        pass