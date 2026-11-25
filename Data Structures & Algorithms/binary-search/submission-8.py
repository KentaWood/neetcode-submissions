class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            m = l + ((r - l) // 2)

            # print(nums[m], m)
            
            if nums[m] > target:
                
                r = m - 1
                # print("1")
            elif nums[m] < target:
                l = m + 1
                # print("2")
                # print(l, r)
            
            else:
                # print("3")
                return m

        return -1

            
        