class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        char = ['+','*','-','/']

        stack = []

        for t in tokens:

            if t not in char:
                stack.append(int(t))

            else:
                sec = stack.pop()
                fir = stack.pop()
                match t:
                    case "*":
                        stack.append(fir * sec)
                    case "/":
                        stack.append(int(fir / sec))
                    case "-":
                        stack.append(fir - sec)
                    case "+":
                        stack.append(fir + sec)
                    case _:
                        print(error)
        
        return stack.pop()
        