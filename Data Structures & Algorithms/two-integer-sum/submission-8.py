class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        sorted_with_idx = [ (num,i)for i, num in enumerate(nums)]
        # print(sorted_with_idx)

        l,r = 0, len(nums) - 1

        while l < r:

            total = sorted_with_idx[l][0] + sorted_with_idx[r][0]

            if total == target:
                l_idx = sorted_with_idx[l][1]
                r_idx = sorted_with_idx[r][1]
                return [l_idx, r_idx] if l_idx < r_idx  else [r_idx, l_idx]

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

        

        