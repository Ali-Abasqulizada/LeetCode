class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        check = sorted(heights)
        ans = 0
        for i in range(len(check)):
            if check[i] != heights[i]:
                ans += 1
        return ans