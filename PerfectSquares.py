'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''

from functools import cache
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        length = n // 2
        check = [i ** 2 for i in range(1, length + 1) if i ** 2 <= n]
        @cache
        def find(money):
            if money == n:
                return 1
            ans = float("inf")
            for c in check:
                if c + money <= n:
                    ans = min(ans, find(money + c) + 1)
            return ans
        return find(0) - 1

#or

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        length = n // 2
        check = [i ** 2 for i in range(1, length + 1) if i ** 2 <= n]
        ans = [float("inf")] * (n + 1)
        ans[0] = 0
        for c in check:
            for a in range(c, n + 1):
                ans[a] = min(ans[a - c] + 1, ans[a])
        return ans[-1]

'''
Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''