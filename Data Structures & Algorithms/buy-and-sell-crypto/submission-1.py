class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, n = 0, len(prices)

        profit = 0
        for right in range(n):
            if prices[left] > prices[right]:
                left = right
            profit = max(profit, prices[right] - prices[left])
        return profit