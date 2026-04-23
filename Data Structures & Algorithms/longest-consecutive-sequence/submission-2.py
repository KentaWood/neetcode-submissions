class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        curr_max = 0

        for num in nums:
            #is a starting number
            if num - 1 not in numset:
                i = 0
                # print(num + i, i)
                # print(numset)
                while num + i in numset:
                    i += 1

                curr_max = max(curr_max, i)

        
        return curr_max

