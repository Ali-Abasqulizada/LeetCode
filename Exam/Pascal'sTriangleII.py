class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        check = [1, 1]
        while rowIndex >= 2:
            rowIndex -= 1
            helper = [1] * (len(check) + 1)
            for i in range(1, len(check)):
                helper[i] = check[i] + check[i - 1]
            check = helper
        return check
    
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