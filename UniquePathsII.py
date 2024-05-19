'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        ans = [0] * cols
        ans[-1] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c]:
                    ans[c] = 0
                elif c + 1 < cols:
                    ans[c] += ans[c + 1]
        return ans[0]

#or

class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        check = [0] * cols
        check[0] = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    check[c] = 0
                elif c > 0:
                    check[c] += check[c - 1]
        return check[-1]

#or

from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        @cache
        def find(i, j):
            if i >= rows or j >= cols or grid[i][j]:
                return 0
            elif i == rows - 1 and j == cols - 1:
                return 1
            return find(i + 1, j) + find(i, j + 1)
        return find(0, 0)

'''
Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
'''