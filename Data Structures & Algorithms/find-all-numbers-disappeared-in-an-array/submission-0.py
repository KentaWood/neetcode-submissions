class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        seen = [False for _ in range(len(nums))]
        ans = []
        
        for num in nums:
            
            seen[num - 1] = True

        print(seen)

        return [ i + 1 for i, val in enumerate(seen) if not val]
        
        