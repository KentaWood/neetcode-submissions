class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def bt(perm,op, cp):

            if op == n and cp == n:
                res.append("".join(perm[:]))
                return 
            
            if op < n:
                perm.append("(")
                bt(perm, op + 1, cp)
                perm.pop()

            if op > cp:
                perm.append(")")
                bt(perm,op, cp + 1)
                perm.pop()

        bt([],0,0)


        return res

