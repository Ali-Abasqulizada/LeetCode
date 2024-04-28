'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
'''

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        def find(r, c, ans, visit):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit:
                return False
            ans += board[r][c]
            visit.add((r, c))
            if ans not in word:
                visit.remove((r, c))
                return False
            elif ans == word:
                return True
            res = find(r + 1, c, ans, visit) or \
                    find(r - 1, c, ans, visit) or \
                    find(r, c + 1, ans, visit) or \
                    find(r, c - 1, ans, visit)
            visit.remove((r, c))
            return res
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if find(r, c, "", set()): return True
        return False
    
'''
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''