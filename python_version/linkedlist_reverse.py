def reverse_linked_list(head):     # More practice, compare this with reverse linkedlist in a range
    if head is None or head.next is None:
        return head

    prev = None
    cur = head

    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    head = prev

    return head