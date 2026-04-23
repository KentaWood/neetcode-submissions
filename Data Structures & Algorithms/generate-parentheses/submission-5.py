class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        stack = []
        res = []

        def backtrack(op:int, cp:int) -> None:

            if op == n and cp == n:
                res.append("".join(stack))

            if op < n:
                stack.append("(")
                backtrack(op + 1, cp)
                stack.pop()

            if cp < op:
                stack.append(")")
                backtrack(op, cp + 1)
                stack.pop()

        backtrack(0,0)
        return res


