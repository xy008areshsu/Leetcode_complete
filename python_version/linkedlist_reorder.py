"""
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    # def __repr__(self):
    #     items = []
    #
    #     cur = self
    #     while cur is not None:
    #         items.append(cur.val)
    #         cur = cur.next
    #
    #     return items.__repr__()


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):   # More practice
        if head is None or head.next is None:
            return head

        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None
        right = self.reverse(right)
        left = self.merge(left, right)

        head = left

    def find_mid(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):  # compare this with reverse linkedlist in a range
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head = prev

        return head

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        dummy = ListNode(0)
        cur = dummy
        cur_left = left
        cur_right = right
        count = 0
        while cur_left and cur_right:
            if count == 0:
                cur.next = cur_left
                cur_left = cur_left.next
                count = 1
            else:
                cur.next = cur_right
                cur_right = cur_right.next
                count = 0
            cur = cur.next

        if cur_left:
            cur.next = cur_left

        if cur_right:
            cur.next = cur_right

        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol.reorderList(head)
    cur = head
    while cur:
        print cur.val
        cur = cur.next
