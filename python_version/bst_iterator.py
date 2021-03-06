"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.st = []
        cur = root
        while cur:
            self.st.append(cur)
            cur = cur.left


    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.st) > 0:
            return True
        return False


    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            node = self.st.pop()
            res = node.val
            node = node.right
            while node:
                self.st.append(node)
                node = node.left
            return res
        return None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())