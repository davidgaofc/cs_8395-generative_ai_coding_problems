from problems.problem_34 import TreeNode, TreeOperations

def test_count_nodes():
    # Create a binary tree:     10
    #                         /    \
    #                       5      15
    #                     /  \    /   \
    #                   3    7  12   18
    binary_tree = TreeOperations([10, 5, 15, 3, 7, 12, 18])
    assert binary_tree.count_nodes() == 7

def test_sum_values():
    binary_tree = TreeOperations([10, 5, 15, 3, 7, 12, 18])
    assert binary_tree.sum_values() == 70

def test_height():
    binary_tree = TreeOperations([10, 5, 15, 3, 7, 12, 18])
    assert binary_tree.height() == 3