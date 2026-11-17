class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        keys = set(s1)
        
        l = 0
        r = 0
        while(r < len(s2)):
            
            if s2[l] not in keys:
                l += 1
                r += 1 
            else:
                seen = set()
                
                while( (r < len(s2)) and (s2[r] in keys )and( s2[r] not in seen) ):
                    seen.add(s2[r])
                    r += 1
                
                if len(seen) == len(keys):
                    return True
                
                l = r
        
        return False