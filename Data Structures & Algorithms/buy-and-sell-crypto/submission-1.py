class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        x = 0
        y = 1

        while y < len(prices):
            temp = prices[y] - prices[x]
            profit = max(temp,profit)
            if temp < 0:
                x += 1
            else:
                y += 1
        return profit