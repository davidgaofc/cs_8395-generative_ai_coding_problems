from problems.problem_70 import BinarySearchTree

def test_insert():
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(1)
    bst.insert(4)

    assert bst.search(5)
    assert bst.search(3)
    assert bst.search(8)
    assert not bst.search(2)
    assert not bst.search(6)

def test_search():
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(1)
    bst.insert(4)

    assert bst.search(5)
    assert bst.search(3)
    assert bst.search(8)
    assert not bst.search(2)
    assert not bst.search(6)