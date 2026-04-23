class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        start = n

        while start not in visit:
            visit.add(start)
            found = 0  # ✅ reset here!

            for d in str(start):
                found += int(d) ** 2

            if found == 1:
                return True

            start = found  # ✅ move to next number
        
        return False
