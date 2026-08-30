class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # split = s.split()


        # return len(split[-1])
        
        #first letter


        
        length = 0
        p = len(s) - 1

        # index of last non space
        while s[p] == " ":
            p -= 1 


        # count number of contigurois no-empty seq of chars
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1 
            

        return length 

         
        