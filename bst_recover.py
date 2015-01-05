"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Hide Tags
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):   # this uses O(n) space
        list_aux = []
        vals = []

        self.helper(root, list_aux, vals)
        vals.sort()
        for i in range(len(list_aux)):
            list_aux[i].val = vals[i]

        return root

    def helper(self, root, list_aux, vals):
        if root is None:
            return

        self.helper(root.left, list_aux, vals)
        list_aux.append(root)
        vals.append(root.val)
        self.helper(root.right, list_aux, vals)

