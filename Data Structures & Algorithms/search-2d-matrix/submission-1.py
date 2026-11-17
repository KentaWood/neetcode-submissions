class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        rows,cols  = len(matrix), len(matrix[0]) - 1
        
        
        l, r = 0, rows * cols
        
        def translate(num:int) -> tuple:
            return (num // rows, num % rows )
        
        while (l <= r):
            i = (l + r) // 2
            
            row, col = translate(i)
            print(row , col)
            found = matrix[row][col]

            if target > found:
                l = i + 1
            elif target < found:
                r = i - 1
            else:
                return True
            
        return False 