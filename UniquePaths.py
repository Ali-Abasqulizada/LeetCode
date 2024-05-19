'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            newRow = [1] * n
            for r in range(n - 2, -1, -1):
                newRow[r] = newRow[r + 1] + row[r]
            row = newRow
        return row[0]
  
#or

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        check = [[1 for _ in range(n)] for _ in range(m)]
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                check[r][c] = check[r + 1][c] + check[r][c + 1]
        return check[0][0]

#or

from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def find(r, c):
            if r >= m - 1:
                return 1
            if c >= n - 1:
                return 1
            return find(r + 1, c) + find(r, c + 1)
        return find(0, 0)
   
#or

from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def find(i, j):
            if i <= 0 or j <= 0:
                return 1
            return find(i - 1, j) + find(i, j - 1)
        return find(m - 1, n - 1)

'''
Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''