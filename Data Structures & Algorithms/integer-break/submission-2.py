class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                remaining = i - j

                dp[i] = max(
                    dp[i],
                    j * remaining,
                    j * dp[remaining]
                )

        return dp[n]