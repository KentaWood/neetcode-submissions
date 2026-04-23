class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {"}":"{", "]":"[",")":"("}
        
        for lettter in s:
            if lettter not in closeToOpen:
                stack.append(lettter)
            else:
                if not stack or stack.pop() != closeToOpen[lettter]:
                    return False
        print(stack)
        return not stack