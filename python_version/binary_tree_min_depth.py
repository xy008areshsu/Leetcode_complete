# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0

        if root is not None and root.left is None and root.right is None:
            return 1

        left_min_depth = self.minDepth(root.left)
        right_min_depth = self.minDepth(root.right)
        if left_min_depth == 0:   # BUG PRONE!!! MUST HAVE this
            return right_min_depth + 1
        if right_min_depth == 0:
            return left_min_depth + 1
        return min(left_min_depth, right_min_depth) + 1