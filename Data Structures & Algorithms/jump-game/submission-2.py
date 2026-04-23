class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0

        for i in range(0, len(nums) - 1):

            farthest = max(farthest, i + nums[i])
            # print(farthest, i)

            if farthest <= i:
                return False
            
        return True



        