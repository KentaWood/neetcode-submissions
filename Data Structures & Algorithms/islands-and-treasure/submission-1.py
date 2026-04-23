class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()
        rows, cols = len(grid), len(grid[0])
        level = 1

        # down up right left 
        directions = [(1,0), (-1,0), (0,1),(0,-1)]

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 0:
                    queue.append((row, col))


        while queue:
            length = len(queue)
            
            for _ in range(length):
                row, col = queue.popleft()

                for nr, nc in directions:
                    
                    if 0 <= row + nr < rows and 0 <= col + nc < cols and grid[row + nr][col + nc] == 2147483647:
                        print((row + nr,col + nc), level)
                        grid[row + nr][col + nc] = level
                        queue.append((row + nr, col + nc))
                
            level += 1




        return 