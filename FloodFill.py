'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel 
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), 
and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
'''

from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        check = deque()
        check.append((sr, sc))
        visit = set()
        visit.add((sr, sc))
        rows, cols = len(image), len(image[0])
        while check:
            row, col = check.popleft()
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r, c = dr + row, dc + col
                if 0 <= r < rows and \
                    0 <= c < cols and \
                    (r, c) not in visit and \
                    image[r][c] == image[sr][sc]:
                    check.append((r, c))
                    visit.add((r, c))
                    image[r][c] = color
        image[sr][sc] = color
        return image

#or

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if color == image[sr][sc]:
            return image
        rows, cols = len(image), len(image[0])
        start = image[sr][sc]
        def find(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            elif image[r][c] != start:
                return
            image[r][c] = color
            find(r + 1, c)
            find(r - 1, c)
            find(r, c + 1)
            find(r, c - 1)
        find(sr, sc)
        return image

'''
Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels 
connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
'''