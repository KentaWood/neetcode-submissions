class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # (index, temperature)
        stack = []
        
        for i, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                l_i, l_temp = stack.pop()
                res[l_i] = i - l_i
            
            stack.append((i, temp))
                
            
        
        
        
        return res
            