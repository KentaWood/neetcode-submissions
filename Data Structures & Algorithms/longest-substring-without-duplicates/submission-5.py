class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        l = 0 
        curr_max = 0

        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            # print(seen)?

            curr_max = max(curr_max, len(seen))

        return curr_max
