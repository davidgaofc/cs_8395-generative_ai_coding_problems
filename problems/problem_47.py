#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def move(self, room):
        self.current_room = room

    def take(self, obj):
        self.inventory.append(obj)
        self.current_room.objects.remove(obj)

    def use(self, obj):
        pass  # Implement the use functionality

    def drop(self, obj):
        self.current_room.objects.append(obj)
        self.inventory.remove(obj)