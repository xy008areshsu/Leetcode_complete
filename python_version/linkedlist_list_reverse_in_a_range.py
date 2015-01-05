"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    # def __repr__(self):
    #     res = []
    #     cur = self
    #     while cur:
    #         res.append(cur.val)
    #
    #     return res.__repr__()



class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):  # more practice
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while i < m and cur:  # find the location of m
            cur = cur.next
            prev = prev.next
            i += 1

        if cur is None:    # if m is too large, return None
            return None

        start = cur
        prev_start = prev
        prev = start
        cur = start.next

        while i < n and cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1

        if i == n:   # if n is not too large, i should be equal to n and cur is not None at this point
            prev_start.next = prev
            start.next = cur       # careful, draw picture to confirm this line
            return dummy.next

        return None  # otherwise, return None


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(3)
    head.next = ListNode(5)

    head = sol.reverseBetween(head, 1, 2)


