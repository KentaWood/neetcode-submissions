class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        adj = [(0,1), (1,0), (-1,0),(0,-1)]
        seen = set()
        og = image[sr][sc]

        bfs = [(sr,sc)]

        while bfs:

            row, col = bfs.pop()
        
            seen.add((row,col))
            image[row][col] = color
            
            for nr, nc in adj:
                
                new_cord = (row + nr, nc + col)

                if new_cord not in seen and row + nr >= 0 and row + nr < len(image) and nc + col >= 0 and nc + col < len(image[0]) and image[new_cord[0]][new_cord[1]] == og:
                    bfs.append(new_cord)
            

        return image
