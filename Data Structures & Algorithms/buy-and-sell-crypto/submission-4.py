class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        b = prices[0]

        for s in prices:

            profit = s - b
        
            res = max(profit, res)

            if profit < 0:
                b = s 
        return res
            
