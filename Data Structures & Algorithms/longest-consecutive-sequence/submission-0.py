class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0
        seen = set()
        starts = set()
        
        # creates the set of numbers
        for num in nums:
            if num not in seen:
                seen.add(num)
        
        #creates the numbers of the beging of the seq's
        for num in seen:
            if num - 1 not in seen:
                starts.add(num)
                
        for num in starts:
            curr = 1
            sq = num + 1
            
            while(sq in seen):
                curr += 1
                sq += 1
                
            ans = max(ans,curr)
            
        
        return ans