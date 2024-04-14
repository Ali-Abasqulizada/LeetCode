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
        if color == image[sr][sc]:
            return image
        row, col = len(image), len(image[0])
        check = deque()
        check.append((sr, sc))
        visit = set()
        ans = [(sr, sc)]
        while check:
            r, c = check.popleft()
            if (r, c) not in visit:
                visit.add((r, c))
                val = image[r][c]
                if r > 0 and image[r - 1][c] == val:
                    ans.append((r - 1, c))
                    check.append((r - 1, c))
                if r < row - 1 and image[r + 1][c] == val:
                    check.append((r + 1, c))
                    ans.append((r + 1, c))
                if c > 0 and image[r][c - 1] == val:
                    check.append((r, c - 1))
                    ans.append((r, c - 1))
                if c < col - 1 and image[r][c + 1] == val:
                    check.append((r, c + 1))
                    ans.append((r, c + 1))
        for i, j in ans:
            image[i][j] = color
        return image

#or

class Solution:
    def find(self, image, sr, sc, color, cur):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return 
        elif cur != image[sr][sc]:
            return
        image[sr][sc] = color
        self.find(image, sr + 1, sc, color, cur)
        self.find(image, sr - 1, sc, color, cur)
        self.find(image, sr, sc + 1, color, cur)
        self.find(image, sr, sc - 1, color, cur)
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        self.find(image, sr, sc, color, image[sr][sc])
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