'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''

from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def find(r, c):
            check = deque()
            visit.add((r, c))
            check.append((r, c))
            while check:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = check.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r, c) not in visit and \
                        0 <= r < rows and \
                        0 <= c < cols and \
                        grid[r][c] == "1":
                        check.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    find(r, c)
                    islands += 1
        return islands
    
#or

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    check = deque()
                    check.append((r, c))
                    visit.add((r, c))
                    while check:
                        row, col = check.popleft()
                        for dr, dc in [1, 0], [0, 1], [0, -1], [-1, 0]:
                            rr, cc = dr + row, dc + col
                            if 0 <= rr < rows and \
                                0 <= cc < cols and \
                                (rr, cc) not in visit and \
                                grid[rr][cc] == "1":
                                check.append((rr, cc))
                                visit.add((rr, cc))
                    ans += 1
        return ans

'''
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''