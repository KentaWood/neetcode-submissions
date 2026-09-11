class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board),len(board[0])
        # down, up, right , left
        dire = [(1,0),(-1,0),(0,1),(0,-1)]

        seen = set()

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O" and (r,c) not in seen:

                    surrounded_flag = True

                    region_cords = [(r,c)]
                    seen.add((r,c))
                    # dfs to see if the regoin is sournded 
                    stack = [(r,c)]

                    while stack:

                        cr, cc = stack.pop()

                        # search sournding cords 
                        
                        for dr, dc in dire:

                            nr, nc = cr + dr, cc + dc

                            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                                surrounded_flag = False

                            else: 
                                if board[nr][nc] == "O" and (nr,nc) not in seen:
                                    stack.append((nr,nc))
                                    seen.add((nr,nc))
                                    region_cords.append((nr,nc))


                    # print(region_cords)
                    if surrounded_flag:

                        for row, col in region_cords:
                            board[row][col] = "X"
    



