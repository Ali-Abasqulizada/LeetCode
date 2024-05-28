class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        check = [0] * (len(nums) + 1)
        for i in nums:
            check[i] = 1
        for i in range(1, len(check)):
            if check[i] == 0:
                ans.append(i)
        return ans