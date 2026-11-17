class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()
        found = 0
        start = n
        while found not in visit:

            int_word = str(start)
            found = 0
            for d in int_word:
                found += int(d) ** 2
            
            if found == 1:
                return True
            
            visit.add(found)
        
        return False
        

        