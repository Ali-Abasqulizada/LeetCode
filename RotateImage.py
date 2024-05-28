'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        check = []
        for c in range(cols):
            for r in range(rows - 1, -1, -1):
                check.append(matrix[r][c])
        row, col = 0, 0
        for i in check:
            matrix[row][col] = i
            col += 1
            if col == cols:
                row += 1
                col = 0

'''
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''