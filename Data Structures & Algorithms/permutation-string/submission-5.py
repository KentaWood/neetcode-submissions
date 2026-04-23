from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s2 can't contain any permutation of s1
        if len(s1) > len(s2):
            return False

        # Helper function to compare two character frequency lists
        def checker(count1: list[int], count2: list[int]):
            res = 0
            for i in range(26):  # check all 26 lowercase letters
                res += 1 if count1[i] == count2[i] else 0
            return res == 26  # return True if all 26 match

        # Frequency count arrays for characters a-z
        count1 = [0] * 26  # for s1
        count2 = [0] * 26  # for sliding window in s2

        # Build frequency count of s1
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        # Initialize first window in s2 (first len(s1) characters)
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        # If first window is a match, return True
        if checker(count1, count2):
            return True

        # Slide the window through s2 one character at a time
        for i in range(len(s1), len(s2)):
            # Add new character to the right end of the window
            count2[ord(s2[i]) - ord('a')] += 1
            # Remove old character from the left end of the window
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Check if the new window is a permutation of s1
            if checker(count1, count2):
                return True

        # No matching permutation found
        return False
