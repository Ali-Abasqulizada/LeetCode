'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        check = {}
        def find(i, buying):
            if i >= len(prices):
                return 0
            elif (i, buying) in check:
                return check[(i, buying)]
            cooldown = find(i + 1, buying)
            if buying:
                buy = find(i + 1, not buying) - prices[i]
                check[(i, buying)] = max(buy, cooldown)
            else:
                sell = find(i + 2, not buying) + prices[i]
                check[(i, buying)] = max(sell, cooldown)
            return check[(i, buying)]
        return find(0, True)

#or

from functools import cache
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def find(i, buying):
            if i >= len(prices):
                return 0
            ans = 0
            cooldown = find(i + 1, buying)
            if buying:
                buy = find(i + 1, not buying) - prices[i]
                ans = max(buy, cooldown)
            else:
                sell = find(i + 2, not buying) + prices[i]
                ans = max(sell, cooldown)
            return ans
        return find(0, True)

#or

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

'''
Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0
'''