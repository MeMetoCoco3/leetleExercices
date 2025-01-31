"""
31. Length of Last Word

Write a function solve that returns the length of the last word in a string.
"""


def solve(s):
    return len(s.split()[-1]) if s else 0


print(solve("hola como estas"))
print(solve(""))
