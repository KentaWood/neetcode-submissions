class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # (position, time to reach goal)
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        
        cars.sort(reverse=True)

        stack = []
        print(cars)
        for dist,time in cars:

            if stack and stack[-1] >= time:
                pass
            else:
                stack.append(time)

        
        
        return len(stack)
    