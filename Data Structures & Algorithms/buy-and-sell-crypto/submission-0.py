class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l,r = 0, 1
        
        while(r < len(prices)):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l += 1
            
            r += 1 
            
        return maxP