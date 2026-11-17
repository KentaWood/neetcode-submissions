class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # list of (pos,speed) ordered by pos: ASC
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key= lambda x:x[0] )   
        # times of each fleet of cars
        stack = []
        
        for pos, speed in cars:
            print(stack)
            time = math.ceil( (target-pos) / speed)
            
            if stack and time >= stack[-1]:
                print(stack)
                pass
            else: 
                stack.append(time)
                
        return len(stack)