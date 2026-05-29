class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profitMax = 0, 1, 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                profitMax = max(profitMax, profit)   
            else:
                buy = sell
            
            sell += 1

        return profitMax