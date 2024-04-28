'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        check = [[0] * cols for _ in range(rows)]
        check[0][0] = grid[0][0]
        for r in range(1, rows):
            check[r][0] = check[r - 1][0] + grid[r][0]
        for c in range(1, cols):
            check[0][c] = check[0][c - 1] + grid[0][c]
        for r in range(1, rows):
            for c in range(1, cols):
                check[r][c] = min(check[r - 1][c], check[r][c - 1]) + grid[r][c]
        return check[-1][-1]
    
'''
Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''