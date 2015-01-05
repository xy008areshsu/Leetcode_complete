"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):  # More practice
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        cur = head

        length = 0
        while cur:
            length += 1
            cur = cur.next

        k = k % length

        if k == 0 or k == length:
            return head

        cur = head
        prev = dummy
        i = 1
        while i != length - k + 1:
            prev = prev.next
            cur = cur.next
            i += 1

        while cur.next:
            cur = cur.next

        cur.next = dummy.next
        dummy.next = prev.next
        prev.next = None

        return dummy.next
