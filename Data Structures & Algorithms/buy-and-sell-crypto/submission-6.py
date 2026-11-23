class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        curr_max = 0
        
        for sell in prices:
            print(sell, buy)
            if sell - buy < 0:
                buy = sell
            
            curr_max = max(curr_max, sell - buy)
        return curr_max


        