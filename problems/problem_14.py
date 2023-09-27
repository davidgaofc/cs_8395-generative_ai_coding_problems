#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class File:
    def __init__(self, name, size):
        """
        Represents a file in the file system.

        Args:
            name (str): Name of the file.
            size (int): Size of the file in bytes.
        """
        self.name = name
        self.size = size

class Folder:
    def __init__(self, name):
        """
        Represents a folder in the file system.

        Args:
            name (str): Name of the folder.
        """
        self.name = name
        self.files = []
        self.subfolders = []

    # TODO: Implement this function
    def add_file(self, file):
        """
        Adds a file to the folder.

        Args:
            file (File): File object to be added.
        """
        pass

    # TODO: Implement this function
    def add_subfolder(self, folder):
        """
        Adds a subfolder to the folder.

        Args:
            folder (Folder): Subfolder object to be added.
        """
        pass

class FileSystem:
    def __init__(self):
        """
        Represents a file system with folders and files.

        This class allows users to organize files and folders, and calculate the total size of a folder and its subfolders.
        """
        self.root = Folder("root")

    # TODO: Implement this function
    def get_total_size(self, folder):
        """
        Calculates the total size of a folder and its subfolders.

        Args:
            folder (Folder): Folder to calculate the size for.

        Returns:
            int: Total size in bytes.
        """
        pass