class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf') 
        max_profit = 0       
        for price in prices:
            if price< min_value:
                min_value = price
            else:
                max_profit = max(max_profit, price-min_value)
        return max_profit
            