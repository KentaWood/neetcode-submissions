class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        curr_max = 0

        for num in nums:

            # not a starting point
            if num - 1 in numset:
                continue
            # number is a starting point
            else:
                i = 1
                # print(num)
                while(num + i in numset):
                    i += 1
                
                curr_max = max(curr_max, i)
        
        return curr_max

