"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.max_depth(root.left) - self.max_depth(root.right)) < 2:
            return True

        return False


    def max_depth(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


