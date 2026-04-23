class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) - 1

        while l <= r:

            m = (r + l) // 2

            if nums[m] == target:
                return m

            # right side is sorted
            if nums[l] > nums[m]:
                
                # m is not in the sorted array
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
            
            # left half is sorted
            else:
                
                # target is not is left sorted array
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
        