class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1 for _ in range(n)] for _ in range(m)]
        print(dp)

        for row in range(1,m):
            for col in range(n):

                print(row - 1,col)
                up = dp[row - 1][col] if 0 <= row - 1 < m else 0
                left = dp[row][col - 1] if 0 <= col - 1 < n else 0

                dp[row][col] = up + left


        # print(dp)

        return dp[-1][-1]
        