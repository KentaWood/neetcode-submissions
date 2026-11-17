class Solution:
    def isValid(self, s: str) -> bool:

        s = []
        CloseToOpen = {"]":"[", "}": "{", ")" : "("}

        for p in s:
            if c in CloseToOpen:
                if stack and stack.peek() == CloseToOpen[p]:
                    stack.pop()
                else:
                    return False

            else:
                stack.push(p)
        
        return True if not s else False 
            
        
                
        