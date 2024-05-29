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