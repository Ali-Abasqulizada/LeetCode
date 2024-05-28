from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        visit = set()
        def find(i, j):
            check = deque()
            check.append((i, j))
            visit.add((i, j))
            count = 1
            while check:
                r, c = check.popleft()
                for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
                    rr, cc = dr + r, dc + c
                    if 0 <= rr < rows and 0 <= cc < cols and (rr, cc) not in visit and grid[rr][cc]:
                        count += 1
                        visit.add((rr, cc))
                        check.append((rr, cc))
            return count
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visit and grid[i][j]:
                    ans = max(ans, find(i, j))
        return ans