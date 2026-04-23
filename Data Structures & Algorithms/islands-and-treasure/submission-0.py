class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque()

        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == 0:
                    q.append((row,col))
        level = 0 

        while q:   
            level += 1
            chests = len(q)

            for _ in range(chests):
                
                row, col = q.popleft()

                for nr, nc in directions:
                    
                    s_row, s_col = nr + row, nc + col

                    if 0 <= s_row < rows and 0 <= s_col < cols and grid[s_row][s_col] != -1 and grid[s_row][s_col] == 2_147_483_647 :
                        
                        grid[s_row][s_col] = level
                        q.append((s_row, s_col))









        