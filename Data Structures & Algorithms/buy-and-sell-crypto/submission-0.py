class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_profit = 0
        min_profit = prices[0]
        profit = 0


        for i in range(len(prices)):
            min_profit = min(prices[i], min_profit )

            profit = prices[i]- min_profit
            max_profit = max(profit, max_profit)

        return max_profit
        