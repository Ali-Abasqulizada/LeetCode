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