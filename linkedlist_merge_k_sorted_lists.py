"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        return self.helper(lists, 0, len(lists) - 1)

    def helper(self, lists, start, end):
        if end == start:
            return lists[start]
        if end - start == 1:
            return self.mergeTwoLists(lists[start], lists[end])

        mid = start + (end - start) // 2
        left_merged = self.helper(lists, start, mid)
        right_merged = self.helper(lists, mid + 1, end)
        return self.mergeTwoLists(left_merged, right_merged)

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


if __name__ == '__main__':
    lists = [ListNode(2), None, ListNode(-1)]
    sol = Solution()
    head = sol.mergeKLists(lists)
    print(head.val)
    print(head.next.val)
    lists1 = [ListNode(-10, ListNode(-9, ListNode(-9, ListNode(-3, ListNode(-1, ListNode(-1, ListNode(0))))))), ListNode(-5),
              ListNode(4), ListNode(-8),None, ListNode(-9, ListNode(-6, ListNode(-5, ListNode(-4, ListNode(-2, ListNode(-2, ListNode(3))))))),
              ListNode(-3, ListNode(-3, ListNode(-2, ListNode(-1, ListNode(0)))))]

    head1 = sol.mergeKLists(lists1)