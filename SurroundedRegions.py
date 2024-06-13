'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        check, visit = set(), set()
        for j in range(cols):
            if board[0][j] == "O":
                check.add((0, j))
            if board[rows - 1][j] == "O":
                check.add((rows - 1, j))
        for i in range(rows):
            if board[i][0] == "O":
                check.add((i, 0))
            if board[i][cols - 1] == "O":
                check.add((i, cols - 1))
        def find(i, j):
            helper = deque()
            helper.append((i, j))
            visit.add((i, j))
            board[i][j] = '!'
            while helper:
                r, c = helper.popleft()
                for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
                    rr, cc = r + dr, dc + c
                    if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == "O" and (rr, cc) not in visit:
                        visit.add((rr, cc))
                        board[rr][cc] = '!'
                        helper.append((rr, cc))
        for i, j in check:
            if (i, j) not in visit:
                find(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "!":
                    board[i][j] = "O"

#or

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        check, visit = set(), set()
        for j in range(cols):
            if board[0][j] == "O":
                check.add((0, j))
            if board[rows - 1][j] == "O":
                check.add((rows - 1, j))
        for i in range(rows):
            if board[i][0] == "O":
                check.add((i, 0))
            if board[i][cols - 1] == "O":
                check.add((i, cols - 1))
        def find(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != "O" or (i, j) in visit:
                return
            visit.add((i, j))
            board[i][j] = "!"
            find(i + 1, j)
            find(i - 1, j)
            find(i, j + 1)
            find(i, j - 1)
        for i, j in check:
            if (i, j) not in visit:
                find(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "!":
                    board[i][j] = "O"


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