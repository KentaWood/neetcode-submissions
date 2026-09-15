class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #number : index 
        seen = defaultdict(int)

        for i,num in enumerate(nums):
            find = target - num

            if find in seen:
                return [seen[find],i]
            seen[num] = i
        
        return [-1,-1]


        