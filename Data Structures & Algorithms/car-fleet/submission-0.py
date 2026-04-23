class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        # create cars list 
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        revSort_cars = sorted(cars, key=lambda x : x[0],reverse=True)
        
        
        for pos, sp in revSort_cars:
            stack.append((target - pos) / sp)
            
            print(stack)
            if len(stack) >= 2 and (stack[-1] <= stack[-2]):
                stack.pop()
            
            
            
            
        
        return len(stack)