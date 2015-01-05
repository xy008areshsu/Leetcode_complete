"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        c = 0
        l1_cur = l1
        l2_cur = l2

        dummy = ListNode(0)
        cur = dummy

        while l1_cur and l2_cur:
            res = l1_cur.val + l2_cur.val + c
            if res > 9:
                res -= 10
                c = 1
            else:
                c = 0
            cur.next = ListNode(res)
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next
            cur = cur.next

        while l1_cur:
            res = l1_cur.val + c
            if res > 9:
                res -= 10
                c = 1
            else:
                c = 0
            cur.next = ListNode(res)
            l1_cur = l1_cur.next
            cur = cur.next

        while l2_cur:
            res = l2_cur.val + c
            if res > 9:
                res -= 10
                c = 1
            else:
                c = 0
            cur.next = ListNode(res)
            l2_cur = l2_cur.next
            cur = cur.next

        if c == 1:
            cur.next = ListNode(c)


        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(0)
    l2 = ListNode(0)
    res = sol.addTwoNumbers(l1, l2)
    print(res.val)