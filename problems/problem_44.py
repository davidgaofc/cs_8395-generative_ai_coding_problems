from typing import List

class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.connections = {}

    def add_user(self, username: str) -> None:
        # Implement this function
        pass

    def add_connection(self, user1: str, user2: str) -> None:
        # Implement this function
        pass

    def get_friends(self, username: str) -> List[str]:
        # Implement this function
        pass

    def are_connected(self, user1: str, user2: str) -> bool:
        # Implement this function
        pass

    def get_common_friends(self, user1: str, user2: str) -> List[str]:
        # Implement this function
        pass

    def get_user_with_max_friends(self) -> str:
        # Implement this function
        pass