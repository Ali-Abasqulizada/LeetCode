'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        left = 0
        right = 1
        for _ in range(n):
            left, right = right, left + right
        return right

#or
    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ans = [0] * n
        ans[0] = 1
        ans[1] = 2
        for i in range(2, n):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[-1]

'''
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''