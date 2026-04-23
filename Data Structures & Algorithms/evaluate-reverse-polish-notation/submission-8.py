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
                        stack.append(fir * sec)
                    case "/":
                        stack.append(int(fir / sec))
                    case "-":
                        stack.append(fir - sec)
                    case "+":
                        stack.append(fir + sec)
                    case _:
                        print(error)
        
        return int(stack.pop())
        