class Process:
    def __init__(self, process_id, burst_time):
        """
        Represents a process in the process scheduling simulator.

        Args:
            process_id (int): Unique identifier for the process.
            burst_time (int): Time required for the process to complete.
        """
        self.process_id = process_id
        self.burst_time = burst_time

class Scheduler:
    def __init__(self):
        """
        Represents a process scheduler in the process scheduling simulator.

        This class allows users to add processes and simulate process scheduling.
        """
        self.processes = []

    # TODO: Implement this function
    def add_process(self, process):
        """
        Adds a process to the scheduler's queue.

        Args:
            process (Process): Process object to be added.
        """
        pass

    # TODO: Implement this function
    def simulate_scheduling(self):
        """
        Simulates process scheduling using a scheduling algorithm.

        Returns:
            List[int]: List of process IDs in the order they are scheduled.
        """
        pass