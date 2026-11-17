class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()
        found = 0
        start = n

        while found not in visit:
            
            visit.add(found)

            found = 0
            for d in str(start):
                found += int(d) ** 2
            
            if found == 1:
                return True
            
        
        return False
        

        