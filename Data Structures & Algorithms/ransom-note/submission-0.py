class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counts = Counter(magazine)

        for let in ransomNote:

            if counts[let] < 1:
                return False
            
            
            counts[let] -= 1

        
        return True
        