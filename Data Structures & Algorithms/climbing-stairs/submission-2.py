class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1 

        if n == 2:
            return 2

        dp = [1] * (n + 1)

        for i in range(2,n + 1):
            print(dp[i - 1 ],dp[i - 2])
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp)

        return dp[-1]

