class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_seen = defaultdict(set)
        row_seen = defaultdict(set)
        grid_seen = defaultdict(set)

        for col in range(0, 9):
            for row in range(0,9):
                square = board[col][row]
                
                if square != ".":
                    num = int(square) 
                    grid = (col // 3) * 3 + row // 3 

                    if (num in row_seen[row] or num in col_seen[col] or num in grid_seen[grid]):
                        return False 
                
                    row_seen[row].add(num)
                    col_seen[col].add(num)
                    grid_seen[grid].add(num)

        return True 