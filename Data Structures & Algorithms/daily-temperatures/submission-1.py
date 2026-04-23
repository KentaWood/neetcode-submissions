class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        #putting (temp,index )
        stack = []
        
        for i, temp in enumerate(temperatures):
            
            while(stack and temp > stack[-1][0]):
                update = stack.pop()
                res[update[1]] = i - update[1]
            
            stack.append((temp, i))
        
        return res  