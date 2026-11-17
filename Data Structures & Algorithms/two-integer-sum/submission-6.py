class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()

        l,r = 0, len(nums) - 1

        while l < r:

            total = nums[l] + nums[r]

            if total == target:
                return [l,r]

            # the total is smaller so we need to increase the toal by incremtning the left pointer
            elif total < target:
                l += 1
            
            else:
                r -= 1

        
        
        # 1. N time N space 
        # seen = defaultdict(int)

        # for i,num in enumerate(nums):
        #     # print(seen)

        #     find = target - num

        #     if find in seen.keys():
        #         return [seen[find], i]

        #     else:
        #         seen[num] = i

        # return [-1,-1]

        

        