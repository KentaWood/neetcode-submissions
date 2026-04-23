class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers

        while l <= r:
            i = (l + r) // 2  # Calculate the middle index correctly
            found = nums[i]

            if found == target:
                return i  # Return the index if target is found
            elif target > found:
                l = i + 1  # Move the left pointer to the right
            else:
                r = i - 1  # Move the right pointer to the left

        return -1  # Return -1 if target is not found
