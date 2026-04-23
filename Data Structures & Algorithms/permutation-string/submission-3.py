from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1count = [0] * 26 
        for c in s1:
            s1count[ord(c)-ord('a')] += 1

        def checker(s1: List[int], s2: List[int]) -> bool:
            matches = 0
            for i in range(26):
                if s1[i] == s2[i]:
                    matches += 1
            return matches == 26

        s2_count = [0] * 26
        l = 0  # left side of the window

        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            s2_count[idx] += 1

            # If window size is bigger than s1, shrink it
            if r - l + 1 > len(s1):
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if checker(s1count, s2_count):
                return True

        return False
