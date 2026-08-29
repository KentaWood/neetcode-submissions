class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        ones = s.count('1') - 1
        ans = ""
        
        for i in range(len(s) - 1):
            print(ans)
            if ones != 0:
                ans += "1"
                ones -= 1
            else:
                ans += "0"



            

 

        return  ans + "1"


        