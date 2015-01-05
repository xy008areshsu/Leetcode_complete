"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:   # More practice, memorize
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None: return None
        fast = slow = head
        hasCycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        if not hasCycle: return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

if __name__ == '__main__':
    head = ListNode(1)
    head.next = head
    # tail = head
    # while tail.next is not None:
    #     tail = tail.next
    #
    # tail.next = head
    sol = Solution()
    print(sol.detectCycle(head))