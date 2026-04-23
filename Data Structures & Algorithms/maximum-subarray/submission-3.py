class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = 0
        curr_max = float("-inf")

        for num in nums:
            curr += num

            curr_max = max(curr, curr_max)
            
            if curr < 0:
                curr = 0
            
        
        return curr_max

        