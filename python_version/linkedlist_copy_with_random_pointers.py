"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None

        dummy = RandomListNode(0)
        new_cur = dummy
        cur = head
        h_map = {}
        while cur:
            new_cur.next = RandomListNode(cur.label)
            new_cur = new_cur.next
            h_map[cur] = new_cur
            cur = cur.next

        cur = head
        new_cur = h_map[head]
        while cur:
            if cur.random in h_map:
                new_cur.random = h_map[cur.random]
            cur = cur.next
            new_cur = new_cur.next

        return dummy.next



