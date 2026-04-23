# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #node, curr max
        stack = [(root, root.val)]
        
        ans = 1

        while stack:
            node, bound = stack.pop()

            if node.right:

                if node.right.val >= bound:
                    ans += 1
                    stack.append((node.right,node.right.val ))
                else:
                    stack.append((node.right, bound))

            if node.left:

                if node.left.val >= bound:
                    ans += 1
                    stack.append((node.left,node.left.val ))
                else:
                    stack.append((node.left, bound))

        return ans
                
                




