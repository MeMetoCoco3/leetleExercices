"""
34. Binary Tree Inorder Traversal

Write a function solve that returns the inorder traversal of a binary tree's nodes' values.

// Note:
// The tests from lettle for this exercice make me think that the binary tree has
// some kind of way to balance itself. So my implementation of a binary tree is not good
// to test it. But seems like my inorder traversal works fine.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def new(values):
        t = TreeNode(val=values[0])
        for v in values[1:]:
            t.add_node(v)
        return t

    def add_node(self, val):
        if val is None:
            return
        if self.val is None:
            self.val = val
            return
        if val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.add_node(val)
        else:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.add_node(val)


def inorder(t):
    val = []
    if t is None:
        return val

    left = inorder(t.left)

    if left is not None:
        val.extend(left)

    val.append(t.val)

    r = inorder(t.right)
    if r is not None:
        val.extend(r)
    return val


def solve(input):
    t = TreeNode.new(input)
    return inorder(t)


print(solve([1, None, 2, 3]))
