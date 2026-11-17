class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)
        
        while(l>r):
            left = s[l]
            right = s[r]
            print(left + "," + right)
            
            if not left.isalpha():
                l +=1
            elif not right.isalpha():
                r -=1       
            else:
                if not left == right:
                    return False
                else:
                    l += 1
                    r -= 1
            
            
        return True
        
        