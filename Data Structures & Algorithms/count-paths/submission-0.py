class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1 for _ in range(m)] for _ in range(n)]

        for row in range(m):
            for col in range(n):

                up = grid[row - 1][col] if 0 <= row - 1 < m else 0
                left = grid[row][col - 1] if 0 <= col - 1 < m else 0

                grid[row][col] = up + left


        print(dp)

        return -1 
        