'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = []
        for row in range(9):
            for col in range(9):
                elem = board[row][col]
                if elem != ".":
                    seen += [(row, elem), (elem, col), (row // 3, col // 3, elem)]
        return len(seen) == len(set(seen))
    
#or
    
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set () for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem == ".":
                    continue
                if elem in row[i] or elem in col[j] or elem in box[i // 3][j // 3]:
                    return False
                row[i].add(elem)
                col[j].add(elem)
                box[i // 3][j // 3].add(elem)
        return True
    
'''
Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''