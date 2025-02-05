def solve(head):
    if head is None:
        return None
    current = fast = head

    while fast.next is not None:
        if fast.next.next is not None:
            current = current.next
            fast = fast.next.next
            continue
        return current.next
    return current
