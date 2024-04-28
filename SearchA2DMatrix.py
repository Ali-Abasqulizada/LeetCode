'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False

#or

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        elif target > matrix[-1][-1] or len(matrix) == 0:
            return False
        row = 0
        while target > matrix[row][-1]:
            row += 1
        low, high = 0, len(matrix[0]) - 1
        while low <= high:
            middle = (low + high) // 2
            if target == matrix[row][middle]:
                return True
            elif target > matrix[row][middle]:
                low = middle + 1
            else:
                high = middle - 1
        return False

'''
Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''