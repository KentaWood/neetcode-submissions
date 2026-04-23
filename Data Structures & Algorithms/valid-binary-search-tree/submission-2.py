# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Stack holds (node, lower_bound, upper_bound)
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, low, high = stack.pop()

            if not node:
                continue

            # If node violates BST rule, return False
            if not (low < node.val < high):
                return False

            # Right child must be greater than current node
            if node.right:
                stack.append((node.right, node.val, high))

            # Left child must be less than current node
            if node.left:
                stack.append((node.left, low, node.val))

        return True
