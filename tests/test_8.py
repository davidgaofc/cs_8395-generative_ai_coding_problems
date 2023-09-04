from problems.problem_8 import file_search
import os

def test_file_search():
    root_dir = "test_files"
    os.makedirs(root_dir, exist_ok=True)

    with open(os.path.join(root_dir, "file1.txt"), "w") as f:
        f.write("Hello, this is file 1.")

    with open(os.path.join(root_dir, "file2.txt"), "w") as f:
        f.write("This is file 2.")

    with open(os.path.join(root_dir, "file3.csv"), "w") as f:
        f.write("CSV data goes here.")

    result = file_search(root_dir, "txt")
    assert len(result) == 2
    assert "file1.txt" in result
    assert "file2.txt" in result

    result = file_search(root_dir, "csv")
    assert len(result) == 1
    assert "file3.csv" in result

    os.remove(os.path.join(root_dir, "file1.txt"))
    os.remove(os.path.join(root_dir, "file2.txt"))
    os.remove(os.path.join(root_dir, "file3.csv"))
    os.rmdir(root_dir)