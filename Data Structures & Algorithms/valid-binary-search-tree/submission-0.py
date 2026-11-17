# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [root]

        while stack:
            
            node = stack.pop()
            # print(node.val)
            if node.right and node.right.val > node.val:
                stack.append(node.right)
            
            else:
                return False
            
            if node.left and node.left.val < node.val:
                stack.append(node.left)
            
            else:
                return False
            
            
        
        return True
        