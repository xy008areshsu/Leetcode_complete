# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        cur1 = l1
        cur2 = l2
        dummy = ListNode(0)
        cur = dummy

        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1 is not None:   # BUG PRONE
            cur.next = cur1

        if cur2 is not None:   # BUG PRONE
            cur.next = cur2

        return dummy.next