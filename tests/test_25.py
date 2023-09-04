from problems.problem_25 import RecursiveTreeTraversal, TreeNode


def test_inorder_traversal():
    traversal = RecursiveTreeTraversal()

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    result = traversal.inorder_traversal(tree)
    assert result == [4, 2, 5, 1, 6, 3, 7]


def test_preorder_traversal():
    traversal = RecursiveTreeTraversal()

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    result = traversal.preorder_traversal(tree)
    assert result == [1, 2, 4, 5, 3, 6, 7]


def test_postorder_traversal():
    traversal = RecursiveTreeTraversal()

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    result = traversal.postorder_traversal(tree)
    assert result == [4, 5, 2, 6, 7, 3, 1]