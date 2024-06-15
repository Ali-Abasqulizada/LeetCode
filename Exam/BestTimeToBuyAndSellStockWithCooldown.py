from functools import cache
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def find(i, buying):
            if i >= len(prices):
                return 0
            ans = 0
            if buying:
                ans = max(find(i + 1, buying), find(i + 1, not buying) - prices[i])
            else:
                ans = max(find(i + 1, buying), find(i + 2, not buying) + prices[i])
            return ans
        return find(0, True)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        rest = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = buy[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sell[i - 1])
        return max(sell[-1], rest[-1])