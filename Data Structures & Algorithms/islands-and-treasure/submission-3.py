class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows,cols = len(grid), len(grid[0])
        dire = ((1,0), (-1,0), (0,1), (0,-1)) 

        bfs = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs.append((r,c))
        
        t = 0
        print(bfs)

        while bfs:

            level = len(bfs)
            t += 1

            print(t,level)
            
            for _ in range(level):
                row, col = bfs.popleft()

                for nr, nc in dire:

                    nrow, ncol = nr + row ,nc + col

                    if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == 2147483647:
                        grid[nrow][ncol] = t
                        bfs.append((nrow, ncol))
        
        return 



        