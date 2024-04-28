'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        startRow, endRow = 0, n - 1
        startCol, endCol = 0, n - 1
        start = 1
        while startRow <= endRow and startCol <= endCol and start <= n ** 2:
            for i in range(startCol, endCol + 1):
                ans[startRow][i] = start
                start += 1
            startRow += 1
            for i in range(startRow, endRow + 1):
                ans[i][endCol] = start
                start += 1
            endCol -= 1
            if startRow <= endRow:
                for i in range(endCol, startCol - 1, -1):
                    ans[endRow][i] = start
                    start += 1
                endRow -= 1
            if startCol <= endCol:
                for i in range(endRow, startRow - 1, -1):
                    ans[i][startCol] = start
                    start += 1
                startCol += 1
        return ans

'''
Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]
'''