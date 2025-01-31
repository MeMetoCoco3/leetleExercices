"""
29. Queue Reconstruction by Height

Write a function solve that reconstructs a queue based on the heights of people and the number of people in front of them. Each person is represented by a pair [h, k], where h is the person's height and k is exactly equal to the number of people in front of this person (BEFORE them in the list) who have a height greater than or equal to h.
"""


def solve(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    print(people)

    queue = []

    for p in people:
        queue.insert(p[1], p)

    return queue


print(
    solve([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
)  # Output: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
