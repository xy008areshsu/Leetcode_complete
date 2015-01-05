"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):   # More practice
        if head is None:
            return None

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left = left_dummy
        right = right_dummy

        cur = head
        while cur:
            if cur.val >= x:
                right.next = ListNode(cur.val)
                right = right.next
            else:
                left.next = ListNode(cur.val)
                left = left.next
            cur = cur.next

        left.next = right_dummy.next
        return left_dummy.next



