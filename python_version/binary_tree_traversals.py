# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal_iterative(self, root):
        if root is None:
            return []

        res = []
        stack = []

        stack.append(root)

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    def inorder_iterative(self, root):  # more practice
        if root is None:
            return []

        res = []
        stack = []

        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left

        while stack:
            node = stack.pop()
            res.append(node.val)
            cur = node.right

            while cur:
                stack.append(cur)
                cur = cur.left


        return res


    def post_order_iterative(self, root):   # More practice
        if root is None:
            return []

        stack = []
        res = []

        stack.append([root, False])

        while stack:
            if stack[-1][1] == True:
                res.append(stack.pop()[0].val)
            elif stack[-1][0].left is None and stack[-1][0].right is None:
                res.append(stack.pop()[0].val)
            else:
                stack[-1][1] = True
                if stack[-1][0].right:
                    stack.append([stack[-1][0].right, False])
                if stack[-1][0].left:
                    stack.append([stack[-1][0].left, False])

        return res
