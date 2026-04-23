class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(i + nums[i],farthest)

            if farthest <= i:
                # print(i)
                return False
        
        return True


        