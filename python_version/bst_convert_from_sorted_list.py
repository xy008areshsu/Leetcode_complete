# idea:
# find middle point and its previous point
# recursively generate bst for left and right part
# combine


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):   # More practice!!!  updated version to find prev_mid
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        if head.next.next is None:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            return root

        prev_mid, mid = self.find_mid(head)
        left_head = head
        right_head = mid.next
        prev_mid.next = None
        left_root = self.sortedListToBST(left_head)
        right_root = self.sortedListToBST(right_head)
        root = TreeNode(mid.val)
        root.left = left_root
        root.right = right_root
        return root

    def find_mid(self, head):
        if head is None:
            return None, None

        if head.next is None:
            return None, head

        if head.next.next is None:
            return head, head.next

        if head.next.next.next is None:
            return head, head.next

        slow = head
        fast = head.next
        dummy = ListNode(0)
        dummy.next = head
        prev_mid = dummy
        while fast and fast.next:
            # if fast.next.next is None or fast.next.next.next is None:  # Careful!!!!
            #     prev_mid = slow
            prev_mid = prev_mid.next
            slow = slow.next
            fast = fast.next.next

        return prev_mid, slow



if __name__ == '__main__':
    sol = Solution()
    head = ListNode(3)
    head.next = ListNode(5)
    head.next.next = ListNode(8)

    print(sol.sortedListToBST(head).val)
