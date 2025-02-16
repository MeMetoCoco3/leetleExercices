"""
46. Container With Most Water

Write a function solve that finds two lines that together with the x-axis forms a container, such that the container contains the most water.
"""


def solve(height):
    stack = []
    res = 0

    for i, cur_h in enumerate(height):
        while stack and cur_h > height[stack[-1]]:
            print("Current", cur_h)
            popped_Idx = stack.pop()  # bottom

            if stack:
                print("Stack: ", stack)

                heightVal = min(height[stack[-1]], cur_h) - height[popped_Idx]

                print("Height val: ", heightVal)
                length = i - stack[-1] - 1
                res += heightVal * length

        stack.append(i)

    return res


print(solve([1, 8, 6, 2, 5, 4, 8, 3, 7]))
