class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1


        while l < r:


            # grab next valid left check
            while l < r and not s[l].isalnum():
                
                l += 1
            # grab next valid left check
            while r > l and not s[r].isalnum():

                r -= 1
            
            print(s[l],s[r])
            # the comparing resutls in a mismatch
            if s[l].lower() != s[r].lower():
                return False
            
            # matcehd for this iteration
            l += 1
            r -= 1
        return True
            


            
        