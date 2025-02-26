def solve(s):
    if s == s[::-1]:
        return True
    options = []
    curr = 0
    while curr < len(s):
        newS = s[:curr] + s[curr + 1 :]
        options.append((newS, newS[::-1]))

        curr += 1
    results = [False if x[0] != x[1] else True for x in options]
    return any(results)


def solve2(s):
    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1
    return True


print(solve("abca"))
