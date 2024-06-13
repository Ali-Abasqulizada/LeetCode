'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        ans = 0
        def find(r, c):
            check = deque()
            check.append((r, c))
            visit.add((r, c))
            count = 1
            while check:
                row, col = check.popleft()
                for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
                    rr, cc = row + dr, col + dc
                    if 0 <= rr < rows and \
                        0 <= cc < cols and \
                        (rr, cc) not in visit and \
                        grid[rr][cc] == 1:
                        visit.add((rr, cc))
                        check.append((rr, cc))
                        count += 1
            return count
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    ans = max(ans, find(r, c))
        return ans

#or

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    count = 1
                    check = deque()
                    check.append((r, c))
                    visit.add((r, c))
                    while check:
                        row, col = check.popleft()
                        for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
                            rr, cc = dr + row, dc + col
                            if 0 <= rr < rows and \
                                0 <= cc < cols and \
                                (rr, cc) not in visit and \
                                grid[rr][cc] == 1:
                                check.append((rr, cc))
                                visit.add((rr, cc))
                                count += 1
                    ans = max(ans, count)
        return ans

#or

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        visit = set()
        def find(i, j, check):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in check or not grid[i][j]:
                return 0
            check.add((i, j))
            return 1 + find(i + 1, j, check) + find(i, j + 1, check) + find(i - 1, j, check) + find(i, j - 1, check)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (i, j) not in visit:
                    ans = max(ans, find(i, j, visit))
        return ans

'''
Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''