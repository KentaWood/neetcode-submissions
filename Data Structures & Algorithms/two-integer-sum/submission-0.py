class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(0,len(nums)):
            find = target - nums[i]
            
            if find in seen:
                return [seen[find],i]
            else:
                seen[nums[i]] =  i
                
        return [-1,-1]