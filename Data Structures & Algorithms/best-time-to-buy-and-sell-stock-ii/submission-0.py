class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        buy = float("inf")

        
        # 5 
        # buy = 1 
        # sell = 5  
        # ans = 4 


        for sell in prices:

            if sell < buy:
                buy = sell
            else:
                ans += sell - buy
                buy = sell


        return ans
        
        