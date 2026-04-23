class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of (position, speed) tuples and sort by position in descending order
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x: x[0], reverse=True)
        # Stack to keep track of fleet times
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / spd
            # If the current car can catch up to the previous fleet, merge them
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)
