class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token.isalnum():
                stack.append(token)
            else:
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                
                if token == "*":
                    stack.append(first_num * second_num)
                    
                elif token == "/":
                    stack.append( first_num // second_num)
                
                elif token == "-":
                    stack.append(first_num - second_num)
                    
                else:
                    stack.append(first_num + second_num)
        
        return stack[-1]