"""
5. Valid Anagram

Write a function solve that determines if two strings are anagrams of each other. An anagram is a word formed by rearranging the letters of another word.

Example:
Input: "listen", "silent"
Output: True
"""


def solve(s1, s2):
    a = [c for c in s1]
    b = [j for j in s2]
    a.sort()
    b.sort()
    return a == b


print(solve("listen", "silent"))
