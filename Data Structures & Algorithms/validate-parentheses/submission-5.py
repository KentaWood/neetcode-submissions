class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []  
        CloseToOpen = {"}":"{", "]":"[", ")":"(" }

        for letter in s:
            if letter not in CloseToOpen:
                stack.append(letter)
            else:
                if not stack or stack.pop() != CloseToOpen[letter]:
                    return False
        
        return not stack
                
    