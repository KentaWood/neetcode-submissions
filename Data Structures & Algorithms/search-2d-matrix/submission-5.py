from typing import List  # This ensures type hints can be used for better clarity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False  # Return False if the matrix is empty or has empty sublists.
        
        rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns properly.
        
        if rows == 0 or cols == 0:
            return False  # If there are no rows or columns, return False.
        
        l, r = 0, rows * cols - 1  # Compute the total elements minus one for the right boundary.
        
        def translate(num: int) -> tuple:
            # Calculate row and column from a linear index num.
            row = num // cols  # Use the number of columns to determine the row.
            col = num % cols  # Use modulus to find the column.
            return (row, col)
        
        while l <= r:
            mid = (l + r) // 2
            row, col = translate(mid)
            found = matrix[row][col]

            if target > found:
                l = mid + 1
            elif target < found:
                r = mid - 1
            else:
                return True
            
        return False
