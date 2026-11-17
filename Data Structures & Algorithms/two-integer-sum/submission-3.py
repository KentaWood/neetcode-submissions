class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(int)

        for num in nums:

            find = num - target

        