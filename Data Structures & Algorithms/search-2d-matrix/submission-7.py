class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        rows,cols  = len(matrix), len(matrix[0])
        
        
        l, r = 0, rows * cols - 1
        
        def translate(num:int) -> tuple:
            return (num // cols, num % cols )
        
        while (l <= r):
            i = (l + r) // 2
            
            row, col = translate(i)
            found = matrix[row][col]

            if target > found:
                l = i + 1
            elif target < found:
                r = i - 1
            else:
                return True
            
        return False 