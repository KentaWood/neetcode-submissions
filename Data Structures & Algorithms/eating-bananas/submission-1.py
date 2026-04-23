class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        

        l = 1
        r = max(piles)
        
        while(l <= r ):
            
            m = (r + l) // 2

            hours = 0
            for pile in piles:
                 hours += math.ceil(pile / m )
            
            # print(hours, m )
            
            if hours > h:
                l = m + 1
            else:
                r = m - 1 


        return l
    
        
        