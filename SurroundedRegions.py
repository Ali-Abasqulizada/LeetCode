'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        check = set()
        for c in range(cols - 1):
            if board[0][c] == "O":
                check.add((0, c))
        for r in range(1, rows):
            if board[r][-1] == "O":
                check.add((r, cols - 1))
        for c in range(cols - 2, -1, -1):
            if board[-1][c] == "O":
                check.add((rows - 1, c))
        for r in range(rows - 2, 0, -1):
            if board[r][0] == "O":
                check.add((r, 0))
        visit = set()
        newCheck = set()
        def find(r, c):
            helper = deque()
            helper.append((r, c))
            visit.add((r, c))
            while helper:
                tr, tc = helper.popleft()
                for dr, dc in [1, 0], [0, 1], [0, -1], [-1, 0]:
                    rr, cc = dr + tr, dc + tc
                    if 0 <= rr < rows and \
                        0 <= cc < cols and \
                        (rr, cc) not in visit and \
                        board[rr][cc] == "O":
                        helper.append((rr, cc))
                        visit.add((rr, cc))
                        newCheck.add((rr, cc))
        for r, c in check:
            if (r, c) not in visit:
                find(r, c)
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if (r, c) not in check and (r, c) not in newCheck:
                    board[r][c] = "X"

#or

from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()
        def find(r, c):
            check = deque()
            check.append((r, c))
            visit.add((r, c))
            board[r][c] = "T"
            while check:
                tr, tc = check.popleft()
                for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
                    rr, cc = dr + tr, dc + tc
                    if 0 <= rr < rows and \
                        0 <= cc < cols and \
                        (rr, cc) not in visit and \
                        board[rr][cc] == "O":
                        board[rr][cc] = "T"
                        visit.add((rr, cc))
                        check.append((rr, cc))
        for c in range(cols):
            if board[0][c] == "O" and (0, c) not in visit:
                find(0, c)
        for r in range(1, rows):
            if board[r][cols - 1] == "O" and (r, cols - 1) not in visit:
                find(r, cols - 1)
        for c in range(cols - 2, -1, -1):
            if board[rows - 1][c] == "O" and (rows - 1, c) not in visit:
                find(rows - 1, c)
        for r in range(rows - 2, 0, -1):
            if board[r][0] == "O" and (r, 0) not in visit:
                find(r, 0)
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

'''
Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
'''