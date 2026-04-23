from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        def checker(count1: list[int], count2: list[int]):
            res = 0

            for i in range(26):
                res += 1 if count1[i] == count2[i] else 0

            return res == 26
        
        count1 = [0] * 26
        count2 = [0] * 26

        # make count1
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        print(count1)
        print(count2)

        if checker(count1, count2):
            return True

        for i in range(len(s1),len(s2)):

            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if checker(count1, count2):
                return True

        
        return False
        
        

