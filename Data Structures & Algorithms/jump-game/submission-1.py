class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curr_reach = 0

        for i, jump in nums.enumerate():

            curr_reach = max(i + jump, curr_reach)

        return curr_reach >= len(nums) - 1


        