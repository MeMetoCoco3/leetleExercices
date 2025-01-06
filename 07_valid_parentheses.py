"""7. Valid Parentheses


Write a function solve that determines if a string s of parentheses is valid. Valid parentheses must be closed in the correct order.

Example:
Input: "()[]{}"
Output: true"""


def solve(s):
    stack = []
    start = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in start:
            stack.append(char)
        elif stack and char == start[stack[-1]]:
            stack.pop(-1)
        else:
            return False
    return not stack


print(solve("[]{}()"))
