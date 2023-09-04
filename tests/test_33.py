from problems.problem_33 import ListNode, LinkedListOperations

def test_insert_at_end():
    linked_list = LinkedListOperations([1, 2, 3])
    linked_list.insert_at_end(4)
    assert linked_list.display() == [1, 2, 3, 4]

def test_find():
    linked_list = LinkedListOperations([1, 2, 3, 4, 5])
    assert linked_list.find(3) == True
    assert linked_list.find(6) == False

def test_delete():
    linked_list = LinkedListOperations([1, 2, 3, 4, 5])
    linked_list.delete(3)
    assert linked_list.display() == [1, 2, 4, 5]

def test_display():
    linked_list = LinkedListOperations([1, 2, 3, 4, 5])
    assert linked_list.display() == [1, 2, 3, 4, 5]