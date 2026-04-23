class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curTotal = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        res = 0
        
        for num in nums:
            
            curTotal += num
            diff = curTotal - k
            res += prefixSum.get(diff, 0)

            prefixSum[curTotal] += 1

        return res 

            


        