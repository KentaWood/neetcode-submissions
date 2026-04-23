class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add closed when open > close
        #only add open when close > open
        # if open == close thne valid
        
        stack = []
        res = []
        
        def backtrack(cp: int , op:int):
            if cp == op == n:
                res.append("".join(stack))
            if op > cp:
                stack.append(")")  
                backtrack(cp + 1, op)
                stack.pop()
            if op < n:
                stack.append("(")
                backtrack(cp , + op + 1)
                stack.pop()
        
            return None 
        backtrack(0,0)
        return res 