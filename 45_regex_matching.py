"""
45. Regular Expression Matching

Write a function solve that implements regular expression matching with support
for '.' and '*'. '.' matches any single character, '*' matches zero or more of
the preceding element.
"""

# Study solution


def solve(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like "a*", ".*", "b*"
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]  # '*' can eliminate the preceding character

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]  # Direct character match or '.'
            elif p[j - 1] == "*":
                # '*' eliminates the preceding character
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                    dp[i][j] |= dp[i - 1][j]  # '*' extends previous match

    return dp[m][n]


print(solve("aaa", "a*"))

# print(solve("mississippi", "mis*is*p*."))
