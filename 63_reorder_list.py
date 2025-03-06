"""
63. Reorder List

Write a function solve that reorders a singly linked list such that the last
element becomes the second element, the second to last element becomes the
4th element, etc.. ie: L0→L1→...→Ln-1→Ln becomes
L0→Ln→L1→Ln-1→Ln2→Ln-2→... it may be useful to look at the
relevant leetcode
"""


def solve(head):
    if not head or not head.next or not head.next.next:
        return head

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, curr = None, slow.next
    slow.next = None  # Break the list into two halves
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    second = prev  # Head of reversed second half

    # Step 3: Merge the two halves
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
    return head
