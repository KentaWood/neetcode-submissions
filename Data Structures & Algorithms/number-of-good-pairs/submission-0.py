class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        def sums(x: int) -> int:
            
            if x == 0:
                return 0

            return x + sums(x - 1)

        counts = Counter(nums)
        ans = 0 

        for num, freq in counts.items():

            if freq >=  2:
                ans += sums(freq - 1)



        return ans

        