class Solution:
    def isValid(self, s: str) -> bool:

        s = deque()

        for par in s:
            if par == ("[" or "{" or "("):
                s.push(par)
            
            else:
                check = s.pop()
                if par == "]": 
                    return check == "["
                elif par == "}":
                    return check == "{}"
        