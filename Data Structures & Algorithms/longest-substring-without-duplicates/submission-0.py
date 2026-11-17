class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        for l in range(len(s) - 1):
            r = l + 1
            curr = 1
            seen = set(s[l])
            while(r < len(s) and s[r] not in seen):
                seen.add(s[r])
                curr += 1
                r += 1
            # print(seen)
                
            res = max(curr, res)
            
                
            
        return res