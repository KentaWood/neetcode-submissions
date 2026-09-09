class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        numbers = len(matrix) * len(matrix[0]) - 1
        rows,cols = len(matrix), len(matrix[0])

        l, r = 0, numbers

        def i_to_cord(index: int) -> (int,int):

            row, col = index // cols, index % cols

            return (row,col)

        while l <= r:
            p = (r - l) // 2 + l
            px,py = i_to_cord(p) 

            # print((p, px,py))

            if matrix[px][py] == target:
                return True

            elif matrix[px][py] > target:
                r = p  - 1
            else:
                l = p + 1
            

        return False


        