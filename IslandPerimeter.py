'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
'''

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 1
                    if i < row - 1 and grid[i + 1][j] == 1:
                        perimeter -= 1
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 1
                    if j < col - 1 and grid[i][j + 1] == 1:
                        perimeter -= 1
        return perimeter
    
'''
Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4
'''