class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        picks = [False] * len(nums)
    
        def backtrack(perm: List[int], picks: List[bool] ):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if not picks[i]:
                    perm.append(nums[i])
                    picks[i] = True
                    backtrack(perm, picks)
                    perm.pop()
                    picks[i] = False
        backtrack([],picks)
        return res


        