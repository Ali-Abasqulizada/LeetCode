'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
'''

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        check = [1, 1]
        while numRows >= 3:
            numRows -= 1
            helper = [1] * (len(check) + 1)
            for i in range(1, len(check)):
                helper[i] = check[i] + check[i - 1]
            check = helper
            ans.append(check)
        return ans

'''
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
'''