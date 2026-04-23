class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        res = 0
        rows, cols = len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1":
                    # print(r,c)
                    res += 1
                    stack = [(r,c)]

                    while stack:
                        sr, sc = stack.pop()

                        grid[sr][sc] = 0

                        for nr, nc in directions:
                            row, col = sr + nr, sc + nc

                            if 0 <= row < rows and 0 <= col< cols and grid[row][col] == "1":
                                stack.append((row, col))
                    
        return res

        
        