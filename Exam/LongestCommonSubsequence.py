from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def find(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            ans = 0
            if text1[i] == text2[j]:
                ans = 1 + find(i + 1, j + 1)
            else:
                ans = max(find(i + 1, j + 1), find(i + 1, j), find(i, j + 1))
            return ans
        return find(0, 0)
    
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        check = [[0] * (len(text2) + 1) for _ in range((len(text1) + 1))]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    check[i][j] = 1 + check[i + 1][j + 1]
                else:
                    check[i][j] = max(check[i + 1][j + 1], check[i + 1][j], check[i][j + 1])
        return check[0][0]