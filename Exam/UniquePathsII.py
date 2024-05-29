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
    
class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        ans = [0] * len(grid[0])
        ans[-1] = 1
        for r in range(len(grid) - 1, -1, -1):
            for c in range(len(grid[0]) - 1, -1, -1):
                if grid[r][c]:
                    ans[c] = 0
                elif c + 1 < len(grid[0]):
                    ans[c] += ans[c + 1]
        return ans[0]