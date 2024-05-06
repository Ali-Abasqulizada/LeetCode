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

'''
Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0
'''