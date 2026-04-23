class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        res = 0
        l = 0

        for r in range(len(s)):

            while l < r and s[r] in seen:
                print(s[l])
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            print(seen)
            res = max(res, len(seen))
        return res
            

