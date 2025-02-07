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


def solve(root):
    def isBalanced(node):
        if not node:
            return 0
        left = isBalanced(node.left)
        right = isBalanced(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return isBalanced(root) != -1
