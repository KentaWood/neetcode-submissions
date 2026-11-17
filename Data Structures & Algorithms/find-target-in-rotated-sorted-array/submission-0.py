class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0,  len(nums) - 1

        while l < r:
            
            m = (r + l) // 2

            found = nums[m]
            
            if found == target:
                return m
            # left half is sorted
            if nums[l] < nums[m]:

                if found < nums[l] or found > nums[m]:
                    l = m + 1
                else:
                    r = m - 1 

            # right half is sorted
            else:
                # if less than middle or more than right than its in the other half
                if found < nums[m] or found > nums[r]:
                    r = m - 1
                else:
                    l = m  + 1 
            
        return -1

