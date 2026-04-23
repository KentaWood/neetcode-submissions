class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {}
        maxf = 0 
        curr_max = 0
        l = 0

        for r,c in enumerate(s):

            counts[c] = counts.get(c, 0) + 1

            maxf = max(maxf, counts[c])

            # window is not valid 
            while (r - l + 1) - maxf  > k:

                counts[s[l]] -= 1
                l += 1
            
            curr_max = max(curr_max, r - l + 1)

            


        return curr_max 


        
        