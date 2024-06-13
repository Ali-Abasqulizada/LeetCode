'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it:
'''

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        check = [1, 1]
        while rowIndex >= 2:
            rowIndex -= 1
            newCheck = [1] * (len(check) + 1)
            for i in range(0, len(check) - 1):
                newCheck[i + 1] = check[i] + check[i + 1]
            check = newCheck
        return check

#or

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        def find(check, i):
            if i == rowIndex:
                return check
            helper = [1] * (len(check) + 1)
            for i in range(1, len(check)):
                helper[i] = check[i - 1] + check[i]
            return find(helper, i + 1)
        return find([1, 1], 0)

'''
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]
'''