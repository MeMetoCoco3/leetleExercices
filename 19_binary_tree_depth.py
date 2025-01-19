"""
19. Binary Tree Maximum Depth

Write a function that finds the maximum depth of a binary tree. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. The tree is represented as an array of nodes in level-order traversal. None indicates empty nodes.
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def print_tree(self):
        if self.val is None:
            return
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()

    def check_depth(self):
        if self.val is None:
            return 0
        l_depth = self.left.check_depth() if self.left else 0
        r_depth = self.right.check_depth() if self.right else 0

        return max(l_depth, r_depth) + 1


def solve(input):
    tree = TreeNode()
    if not input:
        return tree.check_depth()
    tree.add_node(input[0])
    for i in input[1:]:
        tree.add_node(i)
    return tree.check_depth()


print(solve([10, 5, 15, 2, 7]))  # Output: 3
print(solve([1, 2, 3, 4, 5]))  # Output: 5 (Skewed right tree)
print(solve([]))  # Output: 0 (Empty tree)
print(solve([5, 3, 8, 1, 4, 7, 9]))  # Output: 3 (Balanced tree)
print(solve([3, 9, 20, None, None, 15, 7]))
