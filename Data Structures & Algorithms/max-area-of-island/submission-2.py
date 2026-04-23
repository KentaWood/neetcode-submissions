class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0

        rows,cols = len(grid),len(grid[0])

        dire = ((0,1),(0,-1),(1,0),(-1,0))


        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    print(row,col)
                    grid[row][col] = 0

                    stack = [(row,col)]
                    size = 0

                    while stack:
                        
                        r, c = stack.pop()
                        size += 1   

                        

                        for nr, nc in dire:

                            sr, sc = r + nr, c + nc

                            if 0 <= sr < rows and 0 <= sc < cols and grid[sr][sc] == 1:
                                grid[sr][sc] = 0
                                stack.append((sr,sc))

                    res = max(res, size)

        
        return res

        