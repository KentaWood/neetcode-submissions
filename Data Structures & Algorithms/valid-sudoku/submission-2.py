class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        ROW = defaultdict(list)
        COL = defaultdict(list)
        GRID = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                
                grid = (row // 3, col // 3)
                found = board[row][col]

                if (found in ROW[row] or found in COL[col] or found in GRID[grid] )and found != ".":
                    print(found)
                    return False
                
                ROW[row].append(found)
                COL[col].append(found)
                GRID[grid].append(found)

        return True
            

