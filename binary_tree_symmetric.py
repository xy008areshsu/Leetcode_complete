# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True

        if (root.left is None and root.right) or (root.left and root.right is None):
            return False

        if root.left is None and root.right is None:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, root1, root2):
        if (root1 is None and root2) or (root1 and root2 is None):
            return False

        if root1 is None and root2 is None:
            return True

        if root1.val != root2.val:
            return False

        return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)