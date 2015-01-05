"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        res = []
        frontier = collections.deque()
        frontier.append(root)
        count = 0
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

            if count == 0:
                res.append(level)
                count = 1
            elif count == 1:
                level.reverse()
                res.append(level)
                count = 0

        return res