class Solution:
    def isValid(self, s: str) -> bool:

        open_to_close = {"}": "{", "]" : "[", ")": "("}

        stack = []


        for p in s:
            
            # closed paranthesis
            if p in open_to_close:

                if len(stack) < 1 or  open_to_close[p] != stack.pop(): 
                    return False

            else:
                stack.append(p)

        return False if stack else True

                





        