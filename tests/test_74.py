from problems.problem_74 import FileManager

def test_write_file():
    filename = "test_file.txt"
    content = "Hello, World!"
    file_manager = FileManager(filename)
    file_manager.write_file(content)
    read_content = file_manager.read_file()
    assert read_content == content

def test_read_file():
    filename = "test_file.txt"
    content = "Hello, World!"
    file_manager = FileManager(filename)
    file_manager.write_file(content)
    read_content = file_manager.read_file()
    assert read_content == content