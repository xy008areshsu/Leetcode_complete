# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):    # More practice
        single_path_sum, max_path_sum = self.helper(root)
        return max_path_sum

    def helper(self, root):
        if root is None:
            single_path_sum = 0
            max_path_sum = -float('inf')
            return single_path_sum, max_path_sum

        left_single_path_sum, left_max_path_sum = self.helper(root.left)
        right_single_path_sum, right_max_path_sum = self.helper(root.right)

        single_path_sum = max(max(left_single_path_sum, right_single_path_sum) + root.val, root.val)
        max_path_sum = max(left_max_path_sum, right_max_path_sum)
        max_path_sum = max(max_path_sum, left_single_path_sum + root.val, right_single_path_sum + root.val, left_single_path_sum + right_single_path_sum + root.val, root.val)

        return single_path_sum, max_path_sum