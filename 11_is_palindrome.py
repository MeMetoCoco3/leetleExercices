"""
11. Palindrome Check

Write a function solve that checks if a string is a palindrome, considering only alphanumeric characters and ignoring case.`"""


def solve(s):
    f = 0
    l = len(s) - 1
    s = s.lower()
    if len(s) == 2:
        return s[1] == s[0]
    while f < l:
        if not s[f].isalpha():
            f += 1
            continue
        if not s[l].isalpha():
            l -= 1
            continue
        if s[f] != s[l]:
            return False
        f += 1
        l -= 1
    return True


print(solve("A man, a plan, a canal: Panama"))
