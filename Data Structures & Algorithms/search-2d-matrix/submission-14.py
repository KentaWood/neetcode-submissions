class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])


        l = 0 
        r = (rows * cols) - 1

        while l <= r:

            m = l + ((r - l ) // 2)
            search = matrix[m // cols][ m % cols]


            if search < target :
                l = m + 1
            
            elif search > target:
                r = m - 1
            else:
                return True




        return False