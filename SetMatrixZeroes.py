'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        check = []
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    check.append((r, c))
        for r, c in check:
            nrow = r
            while nrow + 1 < rows:
                matrix[nrow + 1][c] = 0
                nrow += 1
            nrow = r
            while nrow - 1 >= 0:
                matrix[nrow - 1][c] = 0
                nrow -= 1
            ncol = c
            while ncol + 1 < cols:
                matrix[r][ncol + 1] = 0
                ncol += 1
            ncol = c
            while ncol - 1 >= 0:
                matrix[r][ncol - 1] = 0
                ncol -= 1

'''
Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''