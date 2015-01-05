"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):  # draw  picture to do it!!!  more practice
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = dummy.next
        start = dummy.next
        prev_start = dummy
        i = 1
        while cur:
            while i < k and cur:
                cur = cur.next
                i += 1
            if start == cur:
                return dummy.next
            if cur is None:
                return dummy.next

            i = 1
            cur2 = start
            while i <= k:
                tmp = cur2.next
                cur2.next = prev
                prev = cur2
                cur2 = tmp
                i += 1
            start.next = tmp
            prev_start.next = cur

            i = 1
            cur = tmp
            prev = start
            prev_start = start
            start = tmp

        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    k = 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = sol.reverseKGroup(head, k)
    print(head.val)
    print(head.next.val)
    print(head.next.next.val)
    print(head.next.next.next.val)
    print(head.next.next.next.next.val)




