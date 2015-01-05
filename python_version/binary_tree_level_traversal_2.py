"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []

        frontier = collections.deque()
        res = []

        frontier.append(root)
        while frontier:
            length = len(frontier)
            level = []
            for i in range(length):
                node = frontier.popleft()
                level.append(node.val)
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)

            res.append(level)

        res.reverse()
        return res