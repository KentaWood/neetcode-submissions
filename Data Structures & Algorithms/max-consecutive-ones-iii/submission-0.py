class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = 0

        for i, l in enumerate(nums):
            
            flips = 0
            curr = 0
            r = 0

            while i + r < len(nums) :
                
                if flips == k and nums[r + i] == 0:
                    break

                elif nums[r + i] == 0:
                    flips += 1 

                
                
                r += 1
                curr += 1
            
            # print(f"current: {i}, count: {curr}")
            
            ans = max(curr, ans)

        return ans



        