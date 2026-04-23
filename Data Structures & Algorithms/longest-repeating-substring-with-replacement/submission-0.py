class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        counts = {}


        l = 0
        maxf = 0
        
        for r in range(len(s)):
            
            counts[s[r]] = counts.get(s[r], 0) + 1 

            #get the highest freq of current iteration
            maxf =  max(maxf, counts[s[r]])
            
            # print(counts)
            
            while r - l + 1 - maxf >  k:
                counts[s[l]] -= 1
                l += 1 
                
                print(s[l: r + 1])


            
            print(s[l: r + 1])
            res = max(res, r - l + 1)
        
        return res

        
        