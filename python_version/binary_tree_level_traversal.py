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
    def levelOrder(self, root):
        if root is None:
            return []

        res = []
        frontier = collections.deque()
        frontier.append(root)
        while frontier:
            level = []
            length = len(frontier)
            for i in range(length):
                node = frontier.popleft()
                level.append(node.val)
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
            res.append(level)

        return res

