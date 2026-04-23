class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(perm,i):

            if i >= len(nums):
                res.append(perm[:])
                return 

            perm.append(nums[i])
            backtrack(perm, i + 1)


            perm.pop()
            backtrack(perm, i + 1)
        
        backtrack([],0)

        return res

        