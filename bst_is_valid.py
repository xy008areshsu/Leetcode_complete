"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        min_val, max_val, is_bst =  self.helper(root)
        return is_bst


    def helper(self, root):
        if root is None:
            return float('inf'), -float('inf'), True

        left_min, left_max, left_valid = self.helper(root.left)
        right_min, right_max, right_valid = self.helper(root.right)

        min_val = min(left_min, right_min, root.val)
        max_val = max(left_max, right_max, root.val)

        if left_valid and right_valid and root.val > left_max and root.val < right_min:
            return min_val, max_val, True
        else:
            return min_val, max_val, False
