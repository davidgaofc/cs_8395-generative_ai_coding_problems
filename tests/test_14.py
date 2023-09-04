from problems.problem_14 import File, Folder, FileSystem

def test_add_file():
    folder = Folder("Documents")
    file = File("report.docx", 2048)
    folder.add_file(file)
    assert len(folder.files) == 1
    assert folder.files[0] == file

def test_add_subfolder():
    parent_folder = Folder("Projects")
    subfolder = Folder("Project A")
    parent_folder.add_subfolder(subfolder)
    assert len(parent_folder.subfolders) == 1
    assert parent_folder.subfolders[0] == subfolder

def test_get_total_size():
    root_folder = Folder("root")
    subfolder1 = Folder("Folder1")
    subfolder2 = Folder("Folder2")
    root_folder.add_subfolder(subfolder1)
    root_folder.add_subfolder(subfolder2)

    file1 = File("file1.txt", 1024)
    file2 = File("file2.txt", 512)
    file3 = File("file3.txt", 256)
    subfolder1.add_file(file1)
    subfolder1.add_file(file2)
    subfolder2.add_file(file3)

    fs = FileSystem()
    total_size = fs.get_total_size(root_folder)
    assert total_size == 1792