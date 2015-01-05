"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):  # use dictionary is simpler and safer than using a set and two pointers.
        if head is None or head.next is None:
            return head

        h_map = {}
        cur = head
        while cur:
            if cur.val not in h_map:
                h_map[cur.val] = 1
            else:
                h_map[cur.val] += 1
            cur = cur.next

        cur = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while cur:
            if h_map[cur.val] > 1:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next


        return dummy.next

