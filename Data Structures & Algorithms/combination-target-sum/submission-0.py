class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def backtrack(perm, i, total):

            if total == target:
                res.append(perm[:])
                return

            if total > target or i >= len(nums):
                return 

            perm.append(nums[i])
            backtrack(perm, i, total + nums[i])

            perm.pop()
            backtrack(perm, i + 1 , total )
        backtrack([], 0, 0)
        return res
