class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphabetic characters from the left
            while l < r and not s[l].isalpha():
                l += 1
            # Skip non-alphabetic characters from the right
            while l < r and not s[r].isalpha():
                r -= 1

            # After skipping, check if pointers have not crossed
            if l >= r:
                break  # Exit the loop as all comparisons are done or invalid

            # Compare the characters
            if s[l].lower() != s[r].lower():
                return False
                
            # Move inward for the next potential alphabetic comparison
            l += 1
            r -= 1
        
        # If all valid comparisons are made without mismatch, it's a palindrome
        return True
