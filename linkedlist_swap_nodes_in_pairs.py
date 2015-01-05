"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):   # More practice
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        i = head
        j = head.next


        while j:      # draw picture!!!
            temp = j.next
            j.next = i
            i.next = temp
            prev.next = j
            if temp and temp.next:
                j = temp.next
                prev = i
                i = temp
            else:
                break

        return dummy.next


