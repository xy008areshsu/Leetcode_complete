"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):  # more practice
        if root is None:
            return

        if root.left is None and root.right is None:
            return

        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)

        if root.left is None:
            return

        cur = root.left
        while cur.right:
            cur = cur.right

        cur.right = root.right
        root.right = root.left
        root.left = None


