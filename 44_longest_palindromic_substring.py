"""
44. Longest Palindromic Substring

Write a function solve that finds the longest palindromic substring in a string.
"""
# Not Resolved yet


def solve(n):
    if n == "":
        return ""
    left = r = 0
    palindromes = []
    for i, _ in enumerate(n):
        if i == 0 or i == len(n):
            continue

        while True:
            breakpoint()
            if not (i - left < 0):
                left -= 1
            if not (r + i >= len(n)):
                r += 1
            curr = n[i - left: i + left]
            if is_palindrome(curr):
                if palindromes and palindromes[-1] == curr:
                    break
                palindromes.append(curr)
            else:
                break
    if not palindromes:
        return ""
    return max(palindromes)


def is_palindrome(n):
    return n == n[::-1]


print(solve("abaxabaxabb"))

print(solve("babd"))
