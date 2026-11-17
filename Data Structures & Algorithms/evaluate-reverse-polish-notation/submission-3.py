class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        char = ['+','*','-','/']

        stack = []

        for t in tokens:

            if t not in char:
                stack.append(t)

            else:
                sec = int(stack.pop())
                fir = int(stack.pop())
                match t:
                    case "*":
                        stack.append(sec * fir)
                    case "/":
                        stack.append(sec // fir)
                    case "-":
                        stack.append(sec - fir)
                    case "+":
                        stack.append(sec + fir)
                    case _:
                        print(error)
        
        return stack.pop()
        