# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):   # updated version
        if len(inorder) != len(preorder):
            return None

        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        root_idx_inorder = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root_idx_inorder = i
        if root_idx_inorder == -1:
            return None

        left_root = self.buildTree(preorder[1: root_idx_inorder + 1], inorder[: root_idx_inorder])    # length of inorder and preorder should be the same
        right_root = self.buildTree(preorder[root_idx_inorder + 1:], inorder[root_idx_inorder + 1: ])

        root.left = left_root
        root.right = right_root

        return root