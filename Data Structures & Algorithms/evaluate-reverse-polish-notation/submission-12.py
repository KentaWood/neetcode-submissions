class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:


            match t:
                case "+":
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(sec + fir)

                case "*":
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(sec * fir)
                case "/":
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(str(int(fir / sec)))

                case "-":
                    sec = int(stack.pop())
                    fir = int(stack.pop())

                    stack.append(fir - sec)

                case _:
                    stack.append(t)
        return int(stack[-1])

        