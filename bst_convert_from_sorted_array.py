# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None

        if len(num) == 1:
            return TreeNode(num[0])

        if len(num) == 2:
            root = TreeNode(num[1])
            root.left = TreeNode(num[0])

        mid = (len(num) - 1) // 2
        root = TreeNode(num[mid])
        left_root = self.sortedArrayToBST(num[: mid])
        right_root = self.sortedArrayToBST(num[mid + 1:])
        root.left = left_root
        root.right = right_root

        return root

