'''
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
'''

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        ans, n = [], len(grid)
        for r in range(1, n - 1):
            check = []
            for c in range(1, n - 1):
                max_ele = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        max_ele = max(max_ele, grid[i][j])
                check.append(max_ele)
            ans.append(check)
        return ans

#or

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        ans, n = [], len(grid)
        for r in range(n - 2):
            check = []
            for c in range(n - 2):
                max_ele = max(grid[r][c], grid[r + 1][c], grid[r + 2][c],
                                grid[r][c + 1], grid[r + 1][c + 1], grid[r + 2][c + 1],
                                grid[r][c + 2], grid[r + 1][c + 2], grid[r + 2][c + 2])
                check.append(max_ele)
            ans.append(check)
        return ans

'''
Example 1:

Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

Example 2:

Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
'''