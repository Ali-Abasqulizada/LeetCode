class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        check = {}
        for i in nums:
            check[i] = check.get(i, 0) + 1
        for i in check:
            if check[i] == 1:
                return i