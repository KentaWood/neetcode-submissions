class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for left in range(len(nums) - 1):

            for right in range(left + 1, left + k + 1):
                
                if right == len(nums):
                    break


                if nums[left] == nums[right]:
                    return True

        
        return False