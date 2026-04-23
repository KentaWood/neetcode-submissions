class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l < r:

            m = (l + r ) // 2

            k = 0
            for pile in piles:
                k += math.ceil(pile / m)
            
            # valid eat per rate
            if k <= h:

                r = m 
            else:
                l = m + 1
        return l

