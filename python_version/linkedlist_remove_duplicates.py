"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head  is None or head.next is None:
            return head

        h_set = set()

        cur = head
        prev = head

        while cur:
            if cur.val not in h_set:
                h_set.add(cur.val)
                prev = cur
                cur = cur.next
            else:
                prev.next = cur.next
                cur = cur.next

        return head