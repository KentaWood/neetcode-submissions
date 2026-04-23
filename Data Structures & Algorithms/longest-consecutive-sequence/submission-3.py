class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        curr_max = 0

        for num in nums:
            
            if num - 1 not in nums:
                i = 0

                while num + i in nums:
                    i += 1
                
                curr_max = max(i, curr_max)
        
        return curr_max
        

