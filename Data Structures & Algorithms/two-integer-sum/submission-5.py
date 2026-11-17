class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(int)

        for i,num in enumerate(nums):
            # print(seen)

            find = target - num

            if find in seen.keys():
                return [seen[find], i]

            else:
                seen[num] = i

        return [-1,-1]

        

        