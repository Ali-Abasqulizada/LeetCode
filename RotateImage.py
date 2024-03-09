mat = [[1,2,3],[4,5,6],[7,8,9]]
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = 0
        for i in range(len(matrix)):
            col = 0
            for j in range(len(matrix[0]) - 1, -1, -1):
                matrix[row][col], matrix[col][row] = matrix[j][i], matrix[j][i]
                col+=1
            row += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print(" ")
result = Solution.rotate(None, mat)
print(result)