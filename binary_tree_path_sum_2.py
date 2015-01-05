"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

import collections
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):  # more practice
        if root is None:
            return []

        res = []
        list_aux = []
        self.helper(root, sum, res, list_aux)

        return res

    def helper(self, root, sum, res, list_aux):
        if root.left is None and root.right is None:
            if sum == root.val:
                list_aux.append(root.val)
                res.append(list_aux[:])
                list_aux.pop()
            return

        list_aux.append(root.val)
        if root.left:
            self.helper(root.left, sum - root.val, res, list_aux)
        if root.right:
            self.helper(root.right, sum - root.val, res, list_aux)
        list_aux.pop()


