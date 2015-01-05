# coding=utf-8
"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# idea:
# compute len_A and len_B
# let the longer one (A or B) go abs(len_A - len_B) steps.
# then do it:
#         while curA and curB:
#             if curA == curB:
#                 return curA
#             curA = curA.next
#             curB = curB.next
#
#         return None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):  # More practice
        if headA is None or headB is None:
            return None

        lenA = 0
        lenB = 0
        cur = headA
        while cur:
            lenA += 1
            cur = cur.next

        cur = headB
        while cur:
            lenB += 1
            cur = cur.next

        cur_A = headA
        cur_B = headB
        if lenA > lenB:
            n = lenA - lenB

            i = 0
            while i != n:
                if cur_A is None:
                    return None
                i += 1
                cur_A = cur_A.next

        else:
            n = lenB - lenA
            i = 0
            while i != n:
                if cur_B is None:
                    return None
                i += 1
                cur_B = cur_B.next

        while cur_A and cur_B:
            if cur_A == cur_B:
                return cur_A
            cur_A = cur_A.next
            cur_B = cur_B.next

        return None




