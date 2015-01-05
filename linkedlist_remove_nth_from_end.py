"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):   # more practice
        if head is None:
            return None

        i = 1
        fast = head
        while i != n:
            if fast is None:
                return None
            i += 1
            fast = fast.next

        slow = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next

        return dummy.next
