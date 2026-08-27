class Solution:
    def scoreOfString(self, s: str) -> int:
        
        ans_list = []

        for i in range(1, len(s)):
            print(i)
            
            ans_list.append(abs(ord(s[i]) - ord(s[i - 1])))

        print(ans_list )

        return sum(ans_list)
        