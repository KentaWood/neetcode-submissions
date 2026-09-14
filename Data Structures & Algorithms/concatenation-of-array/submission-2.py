class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # concatnate two [x] + [x]
        # return nums * 2

        # 
        ans = nums[::]

        for num in nums:
            ans.append(num)

        return ans