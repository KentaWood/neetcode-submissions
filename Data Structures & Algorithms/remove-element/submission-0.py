class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # marker, for whcih index we need to swap with 
        replace = 0
        ans = 0

        for num in nums:


            if num != val:
                nums[replace] = num
                ans += 1
                replace += 1


        return ans

                
             

            