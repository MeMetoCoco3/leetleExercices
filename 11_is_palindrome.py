"""
11. Palindrome Check

Write a function solve that checks if a string is a palindrome, considering only alphanumeric characters and ignoring case.`"""


def solve(s):
    f = 0
    l = len(s) - 1
    s = s.lower()

    while f < l:
        if not s[f].isalnum():
            f += 1
            continue
        if not s[l].isalnum():
            l -= 1
            continue
        if s[f] != s[l]:
            return False
        f += 1
        l -= 1
    return True


def solve2(s):
    s = [c.lower() for c in s if c.isalnum()]
    return s == s[::-1]


print(solve2("A man, a plan, a canal: Panama"))
