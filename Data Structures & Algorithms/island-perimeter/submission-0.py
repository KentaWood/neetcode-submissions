class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0
        rows,cols = len(grid), len(grid[0])
        cords = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                
                    
                    stack = [(row,col)]
                    seen.add((row,col))

                    while stack:
                        
                        

                        r,c = stack.pop()

                        print("cords:", r , c)
                        for dc, dr in cords:

                            
                            nr, nc = r + dr, c + dc

                            if 0 <= nr and nr < rows and 0 <= nc and nc < cols and (nr,nc) not in seen and grid[nr][nc] == 1:
                                # print("here")
                                stack.append((nr,nc))
                                seen.add((nr,nc))

                            else: 
                                if (nr,nc) not in seen:
                                    print(nr,nc)
                                    ans += 1


                    

                    # only one island so we only need to run dfs once 
                    return ans
        
        return -1
        