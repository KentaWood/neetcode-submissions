class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        curr_max = 0
        
        for num in num_set:
            
            if num - 1 not in num_set:
                i = 0

                while num + i in num_set:
                    i += 1
                
                curr_max = max(curr_max, i)
        
        return curr_max


        