# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #te root nod itself is always a good node
        ans = 1
        # the (root node, curr_max of the path)
        stack = [(root,root.val)]

        while stack:
            # print(stack)

            node, curr_max = stack.pop()

            if node.right and node.right.val >= curr_max:
                stack.append((node.right, node.right.val))
                ans += 1 
            else:
                if node.right:
                    stack.append((node.right, curr_max))


            if node.left and node.left.val >= curr_max:
                stack.append((node.left,node.left.val))
                ans += 1
            else:
                if node.left:
                    stack.append((node.left, curr_max))


        return ans
        