class Solution:
    def check(self, nums: List[int]) -> bool:

        mini = min(nums)
        pivot = -1
        length = len(nums)

        for i, num in enumerate(nums):

            
            if nums[i] == mini:
                pivot = i
                break

        # check ordering right of pivot and make sure its number above the max
        prev = mini

        for i in range(pivot,length):

            if prev <= nums[i]:
                prev = nums[i]
            else:
                return False
        
        #check ordering from 0 up to pivot index
        for i in range(pivot):

            if prev <= nums[i]:
                prev = nums[i]
            else:
                return False

        return True




            

        