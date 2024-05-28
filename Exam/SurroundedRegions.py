from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()
        def find(i, j):
            check = deque()
            check.append((i, j))
            visit.add((i, j))
            while check:
                r, c = check.popleft()
                for dr, dc in [1, 0], [0, 1], [-1, 0], [0, -1]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and (rr, cc) not in visit and board[rr][cc] == "O":
                        board[rr][cc] = "U"
                        visit.add((rr, cc))
                        check.append((rr, cc))
        for j in range(cols):
            if board[0][j] == "O" and (0, j) not in visit:
                board[0][j] = "U"
                find(0, j)
        for i in range(1, rows):
            if board[i][cols - 1] == "O" and (i, cols - 1) not in visit:
                board[i][cols - 1] = "U"
                find(i, cols - 1)
        for j in range(cols - 2, -1, -1):
            if board[rows - 1][j] == "O" and (rows - 1, j) not in visit:
                board[rows - 1][j] = "U"
                find(rows - 1, j)
        for i in range(rows - 2, 0, -1):
            if board[i][0] == "O" and (i, 0) not in visit:
                board[i][0] = "U"
                find(i, 0)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "U":
                    board[i][j] = "O"