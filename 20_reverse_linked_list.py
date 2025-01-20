"""
20. Reverse Linked List

Write a function that, given the head of a singly linked list, reverses the list. Return the root node of the reversed list.
"""


def solve(head):
    curr = head
    prev = None

    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next

    return head
