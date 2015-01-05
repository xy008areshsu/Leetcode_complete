"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
import collections
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return

        frontier = collections.deque()
        frontier.append(root)
        while frontier:
            level = []
            length = len(frontier)
            for i in range(length):
                node = frontier.popleft()
                level.append(node)
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
            level[-1].next = None