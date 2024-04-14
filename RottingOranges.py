'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while rotten and fresh > 0:
            minutes += 1
            lenght = len(rotten)
            for _ in range(lenght):
                r, c = rotten.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        continue
                    elif grid[rr][cc] == 0 or grid[rr][cc] == 2:
                        continue
                    fresh -= 1
                    grid[rr][cc] = 2
                    rotten.append((rr, cc))
        return minutes if fresh == 0 else -1

'''
Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''