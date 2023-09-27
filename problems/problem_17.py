#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class Server:
    def __init__(self, server_id, load):
        """
        Represents a server in a distributed system.

        Args:
            server_id (int): Unique identifier for the server.
            load (int): Current load of the server.
        """
        self.server_id = server_id
        self.load = load

class LoadBalancer:
    def __init__(self):
        """
        Represents a load balancer in a distributed system.

        This class allows users to add servers and balance the load.
        """
        self.servers = []

    # TODO: Implement this function
    def add_server(self, server):
        """
        Adds a server to the load balancer.

        Args:
            server (Server): Server object to be added.
        """
        pass

    # TODO: Implement this function
    def balance_load(self):
        """
        Balances the load across all servers.
        """
        pass

    # TODO: Implement this function
    def get_server_with_lowest_load(self):
        """
        Retrieves the server with the lowest load.

        Returns:
            Server: Server object with the lowest load.
        """
        pass