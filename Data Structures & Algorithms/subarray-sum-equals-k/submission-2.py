class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0

        #prefix sum, freq
        prefix = defaultdict(int)
        curr_sum = 0
        
        prefix[0] = 1
        for num in nums:

            curr_sum += num
            # print(prefix, curr_sum)
            
            ans += prefix.get(curr_sum - k, 0)

            prefix[curr_sum] += 1
        
        return ans

