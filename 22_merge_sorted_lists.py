"""
22. Merge Sorted Lists

Write a function solve that merges two sorted lists into one sorted list.
"""


def solve(list1, list2):
    p1 = p2 = 0
    newList = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            newList.append(list1[p1])
            p1 += 1
        else:
            newList.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        newList.extend(list1[p1:])
    else:
        newList.extend(list2[p2:])
    return newList


def solve2(list1, list2):
    new_list = list1 + list2
    return sorted(new_list)


l1 = [1, 5, 7, 8]
l2 = [2, 5, 7, 9, 12, 16]
print(solve2(l1, l2))
