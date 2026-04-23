# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        
        # (node, greatest node val)
        stack = [(root,root.val)]

        while stack:

            node, curr_max = stack.pop()

            if curr_max <= node.val:
                print(node.val)
                res += 1
            
            if node.left:
                stack.append((node.left, max(curr_max, node.val)))

            if node.right:
                stack.append((node.right, max(curr_max, node.val)))



            
        return res




        