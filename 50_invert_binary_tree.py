"""
50. Invert a Binary Tree

Write a function solve that inverts a binary tree. Return the root of the inverted tree.
"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(root):
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    solve(root.left)
    solve(root.right)
    return root
