'''
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        check = [float("inf")] * (amount + 1)
        check[0] = 0
        for c in coins:
            for a in range(c, amount + 1):
                if a - c >= 0:
                    check[a] = min(check[a], check[a - c] + 1)
        return check[-1] if check[-1] != float("inf") else -1

#or

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def find(rem, check):
            if rem < 0:
                return float("inf")
            elif rem == 0:
                return 0
            elif rem in check:
                return check[rem]
            check[rem] = min(find(rem - c, check) + 1 for c in coins)
            return check[rem]
        ans = find(amount, {})
        return ans if ans != float("inf") else -1

#or

from functools import cache
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def find(money):
            if money == amount:
                return 0
            numberOfCoin = float("inf")
            for c in coins:
                if c + money <= amount:
                    numberOfCoin = min(numberOfCoin, 1 + find(money + c))
            return numberOfCoin
        ans = find(0)
        return ans if ans != float("inf") else -1

#or

from functools import cache
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def find(money):
            if money == 0:
                return 0
            numberOfCoin = float("inf")
            for c in coins:
                if money - c >= 0:
                    numberOfCoin = min(numberOfCoin, 1 + find(money - c))
            return numberOfCoin
        ans = find(amount)
        return ans if ans != float("inf") else -1

'''
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
'''