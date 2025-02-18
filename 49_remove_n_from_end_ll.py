"""
49. Remove Nth Node From End of List

Write a function solve that removes the nth node from the end of a singly linked list. Return the head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head, n):
    size = get_len(head)
    if size == n:
        if head.next is not None:
            return head.next
        else:
            return []

    point = head
    for _ in range(size - 1 - n):
        point = point.next
    point.next = point.next.next
    return head


def get_len(head):
    cnt = 1
    while head.next is not None:
        cnt += 1
        head = head.next
    return cnt


def add(head, val):
    while head.next is not None:
        head = head.next
    head.next = ListNode(val)


def print_ll(head):
    r = []
    while head:
        r.append(head.val)
        head = head.next
    return r


l = ListNode(1)


print(print_ll(l))
print(print_ll(solve(l, 1)))
add(l, 2)
add(l, 3)
add(l, 4)
add(l, 5)
add(l, 6)

print(print_ll(l))
print(print_ll(solve(l, 3)))
