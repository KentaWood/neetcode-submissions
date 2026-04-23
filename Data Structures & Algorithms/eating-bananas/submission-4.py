class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1 
        # r = max(piles)
        r = 2 ** 32 - 1

        while l <= r:

            m = (r - l) // 2 + l

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / m)
            
            # can eat the pile make next number smaller 
            if hours <= h:
                r = m - 1
            
            else:
                l = m + 1
        
        return l
