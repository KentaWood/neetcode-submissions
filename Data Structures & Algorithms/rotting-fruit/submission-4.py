class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dire = ((1,0), (-1,0),(0,1),(0,-1))
        rows, cols = len(grid),len(grid[0])
        bfs = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    bfs.append((r,c))
                
                elif grid[r][c] == 1:
                    fresh += 1
        
        t = 0

        while bfs:
            
            if not fresh:
                break

            t += 1
            level = len(bfs)

            
            
            for _ in range(level):
                row, col = bfs.popleft()
                


                for nr,nc in dire:
                    srow, scol = nr + row, nc + col

                    if 0 <= srow < rows and 0 <= scol < cols and grid[srow][scol] == 1:
                        print(t, srow,scol)
                        grid[srow][scol] = 2
                        fresh -= 1
                        bfs.append((srow,scol))

        return t if not fresh else -1 



