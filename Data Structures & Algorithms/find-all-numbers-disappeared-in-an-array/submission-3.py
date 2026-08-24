class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for num in nums:

            x = abs(num)
            
            # mark only if the mark is not negative
            if nums[x - 1] > 0:

                #mark the i as seen
                nums[x - 1] = -nums[x - 1] 
            

            # print(nums, num)

        return [ i + 1 for i, val in enumerate(nums) if val > 0]
        
        