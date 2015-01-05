"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):  # more practice
        if head is None:
            return None

        if head.next is None:
            return head

        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def find_mid(self, head):
        if head is None:
            return None

        if head.next is None:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        dummy = ListNode(0)
        cur = dummy
        cur_left = left
        cur_right = right

        while cur_left and cur_right:
            if cur_left.val < cur_right.val:
                cur.next = cur_left
                cur_left = cur_left.next
            else:
                cur.next = cur_right
                cur_right = cur_right.next
            cur = cur.next

        if cur_left:
            cur.next = cur_left

        if cur_right:
            cur.next = cur_right

        return dummy.next
