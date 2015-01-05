"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:    # Exactly the same as binary_tree_path_sum_2 with DFS!!!!
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):  # more practice
        if root is None:
            return 0

        res = []
        str_aux = ''
        self.helper(root, res, str_aux)

        return sum([int(v) for v in res])

    def helper(self, root, res, str_aux):
        if root.left is None and root.right is None:
            res.append(str_aux + str(root.val))
            return

        str_aux += str(root.val)
        if root.left:
            self.helper(root.left, res, str_aux)
        if root.right:
            self.helper(root.right, res, str_aux)
        str_aux = str_aux[:-1]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(9)
    print(sol.sumNumbers(root))
