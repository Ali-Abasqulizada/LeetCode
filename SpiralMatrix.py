'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        ans = []
        while startRow <= endRow and startCol <= endCol:
            for i in range(startCol, endCol + 1):
                ans.append(matrix[startRow][i])
            startRow += 1
            for i in range(startRow, endRow + 1):
                ans.append(matrix[i][endCol])
            endCol -= 1
            if startRow <= endRow:
                for i in range(endCol, startCol - 1, -1):
                    ans.append(matrix[endRow][i])
                endRow -= 1
            if startCol <= endCol:
                for i in range(endRow, startRow - 1, -1):
                    ans.append(matrix[i][startCol])
                startCol += 1
        return ans

'''
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''