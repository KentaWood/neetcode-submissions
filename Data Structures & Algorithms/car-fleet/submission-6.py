class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # list of (pos,speed) ordered by pos: ASC
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key= lambda x:x[0],reverse=True )   
        # times of each fleet of cars
        stack = []
        
        for pos, speed in cars:
            
            time = (target - pos ) / speed
            
            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
                
        return len(stack) 