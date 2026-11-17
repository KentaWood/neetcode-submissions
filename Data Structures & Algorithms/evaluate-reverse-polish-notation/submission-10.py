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
                    stack.append(int(sec / fir))

                case "-":
                    sec = int(stack.pop())
                    fir = int(stack.pop())

                    stack.append(sec - fir)

                case _:
                    stack.append(t)
        return stack[-1]

        