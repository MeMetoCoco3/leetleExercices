"""
69. Find All Duplicates in an Array

Write a function solve that finds all integers that appear exactly twice in an
array where each integer is in the range [1, n] (inclusive) where n is the size
of the array. Return the list of duplicates in ascending order.
"""

from collections import Counter


def solve(nums):
    c = Counter(nums)
    return sorted([x for x, count in c.items() if count == 2])
