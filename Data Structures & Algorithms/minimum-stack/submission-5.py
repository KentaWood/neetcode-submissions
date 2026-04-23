class MinStack:

    def __init__(self):
        self.stack = []
        self.min  = float('inf')

        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        

    def pop(self) -> None:
        if not self.stack:
            return 
        
        num = self.stack.pop()

        # if the poped num was negative we need to change the current min
        if num < 0:
            self.min = self.min - num

        

    def top(self) -> int:

        num = self.stack[-1]

        if num >= 0:
            return self.stack[-1] + self.min
        else: 
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
